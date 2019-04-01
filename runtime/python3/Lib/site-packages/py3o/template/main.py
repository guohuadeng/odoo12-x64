# -*- encoding: utf-8 -*-
import babel.dates
import babel.numbers
from base64 import b64decode
import codecs
from copy import copy
from datetime import datetime
import decimal
import hashlib
from io import BytesIO
import logging
import locale
import os
import re
import six
from six.moves import urllib
import traceback
from uuid import uuid4
import warnings
from xml.sax.saxutils import escape
import zipfile

import lxml.etree
from PIL import Image
from genshi.template import MarkupTemplate
from genshi.template.text import NewTextTemplate as GenshiTextTemplate
from genshi.filters.transform import Transformer
from genshi.core import Markup
from pyjon.utils import get_secure_filename

if six.PY3:  # pragma: no cover
    # in python 3 we want to emulate  binary files
    from six import BytesIO as StringIO
else:  # pragma: no cover
    # in python 2 we want to try and use the c Implementation if available
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO


log = logging.getLogger(__name__)

# expressed in clark notation: http://www.jclark.com/xml/xmlns.htm
XML_NS = "{http://www.w3.org/XML/1998/namespace}"

GENSHI_URI = "http://genshi.edgewall.org/"
REGEXP_URI = "http://exslt.org/regular-expressions"
PY3O_URI = "http://py3o.org/"
MANIFEST = "META-INF/manifest.xml"


class TemplateException(ValueError):
    """some client code is used to catching ValueErrors, let's keep the old
    codebase happy
    """

    def __init__(self, message):
        """define the __init__ to handle message... for python3's sake
        """
        self.message = message

    def __str__(self):  # pragma: no cover
        return self.message


def detect_keep_boundary(start, end, namespaces):
    """a helper to inspect a link and see if we should keep the link boundary
    """
    result_start, result_end = False, False
    parent_start = start.getparent()

    if parent_start.tag == "{%s}p" % namespaces["text"]:
        # more than one child in the containing paragraph ?
        # we keep the boundary
        result_start = len(parent_start.getchildren()) > 1

    if end is not None:
        parent_end = end.getparent()
        if parent_end.tag == "{%s}p" % namespaces["text"]:
            # more than one child in the containing paragraph ?
            # we keep the boundary
            result_end = len(parent_end.getchildren()) > 1

    return result_start, result_end


def move_siblings(
    start, end, new_, keep_start_boundary=False, keep_end_boundary=False
):
    """a helper function that will replace a start/end node pair
    by a new containing element, effectively moving all in-between siblings
    This is particularly helpful to replace for /for loops in tables
    with the content resulting from the iteration

    This function call returns None. The parent xml tree is modified in place

    @param start: the starting xml node
    @type start: lxml.etree.Element

    @param end: the ending xml node
    @type end: lxml.etree.Element

    @param new_: the new xml element that will replace the start/end pair
    @type new_: lxlm.etree.Element

    @param keep_start_boundary: Flag to let the function know if it copies
    your start tag to the new_ node or not, Default value is False
    @type keep_start_boundary: bool

    @param keep_end_boundary: Flag to let the function know if it copies
    your end tag to the new_ node or not, Default value is False
    @type keep_end_boundary: bool

    @returns: None
    @raises: ValueError
    """
    old_ = start.getparent()
    if keep_start_boundary:
        new_.append(copy(start))

    else:
        if start.tail:
            # copy the existing tail as text
            new_.text = start.tail

    # get all siblings
    for node in start.itersiblings():
        if node is not end:
            new_.append(node)

        elif node is end:
            # if this is already the end boundary, then we are done
            if keep_end_boundary:
                new_.append(copy(node))

            break

    # replace start boundary with new node
    old_.replace(start, new_)

    # remove ending boundary we already copied it if needed
    if end is not None:
        old_.remove(end)


def get_list_transformer(namespaces):
    """this function returns a transformer to
     find all list elements and recompute their xml:id.
    Because if we duplicate lists we create invalid XML.
    Each list must have its own xml:id

    This is important if you want to be able to reopen the produced
     document wih an XML parser. LibreOffice will fix those ids itself
     silently, but lxml.etree.parse will bork on such duplicated lists
    """
    return Transformer(
        '//list[namespace-uri()="%s"]' % namespaces.get("text")
    ).attr("{0}id".format(XML_NS), lambda *args: "list{0}".format(uuid4().hex))


def get_all_python_expression(content_trees, namespaces):
    """Return all the python expressions found in the whole document
    """
    xpath_expr = (
        r"//text:a[starts-with(@xlink:href, 'py3o://')] | "
        r"//text:text-input[starts-with(@text:description, 'py3o://')] | "
        r"//text:user-field-get[starts-with(@text:name, 'py3o.')] | "
        r"//table:table-cell/text:p[regexp:match(text(), '\${[^\${}]*}')] | "
        r"//table:table-cell[regexp:match(@table:formula, '\${[^\${}]*}')]"
    )
    res = []
    for content_tree in content_trees:
        res.extend(content_tree.xpath(xpath_expr, namespaces=namespaces))
    return res


def get_image_frames(content_tree, namespaces):
    """find all draw frames that must be converted to draw:image
    """
    xpath_expr = "//draw:frame[starts-with(@draw:name, 'py3o.image')]"
    return content_tree.xpath(xpath_expr, namespaces=namespaces)


def get_instructions(content_tree, namespaces):
    """find all text links that have a py3o
    """
    xpath_expr = (
        "//text:a[starts-with(@xlink:href, 'py3o://')] | "
        "//text:text-input[starts-with(@text:description, 'py3o://')]"
    )
    return content_tree.xpath(xpath_expr, namespaces=namespaces)


def get_user_fields(content_tree, namespaces):
    field_expr = r"//text:user-field-decl[starts-with(@text:name, 'py3o.')]"
    return content_tree.xpath(field_expr, namespaces=namespaces)


def get_soft_breaks(content_tree, namespaces):
    xpath_expr = "//text:soft-page-break"
    return content_tree.xpath(xpath_expr, namespaces=namespaces)


def format_amount(amount, format="%f"):
    """Replace the thousands separator from '.' to ','
    """

    warnings.warn(
        "The format_locale function is marked for deprecation in 2019, please "
        "use format_currency instead.",
        DeprecationWarning,
    )

    if isinstance(amount, float) or isinstance(amount, decimal.Decimal):
        amount = (format % amount).replace(".", ",")
    return amount


def format_locale(amount, format_, locale_, grouping=True):
    """format the given amount using the format and a locale
    example: format_locale(10000.33, "%.02f", "fr_FR.UTF-8")
    will give you: "10 000,33"
    """

    warnings.warn(
        "The format_locale function is marked for deprecation in 2019, please "
        "use format_currency instead.",
        DeprecationWarning,
    )

    # pragma: nocover
    # Not including this into tests as this was short-lived and now deprecated.

    locale.setlocale(locale.LC_ALL, locale_)
    return locale.format(format_, amount, grouping)


def format_currency(*args, **kwargs):
    """Format the specified amount according to a format string & a currency.

    Relies on babel.numbers.format_currency.

    Online docs:
    * <http://babel.pocoo.org/en/latest/numbers.html#pattern-syntax>
    * <http://babel.pocoo.org/en/latest/api/numbers.html
       #babel.numbers.format_currency>

    Changes we provide here:
    * Make the 2nd argument (currency) optional. When not displaying the
      currency symbol, no need to provide a currency.

    Note: Specifying the "locale" kwarg is recommended; otherwise the default
    system locale will be used.

    Their parameter docstring has been copied below.

    :param number: the number to format
    :param currency: the currency code, optional unless displaying the currency
    :param format: the format string to use
    :param locale: locale identifier - recommended, see above
    :param currency_digits: use the currency's natural number of decimal digits
    :param format_type: the currency format type to use
    :param decimal_quantization: Truncate and round high-precision numbers to
                                 the format pattern. Defaults to ``True``.

    :rtype: String.
    """

    # Make the 2nd argument (currency) optional. When not displaying the
    # currency symbol, no need to provide a currency.
    if len(args) < 2:
        args += ("",)  # empty "currency" arg

    return babel.numbers.format_currency(*args, **kwargs)


ISO_DATE_FORMAT = "%Y-%m-%d"
ISO_DATETIME_FORMAT = ISO_DATE_FORMAT + " %H:%M:%S"


def format_date(date, format=ISO_DATE_FORMAT):
    """Format the date according to format string.

    :param date: One of: datetime.date object, datetime.datetime object, ISO
    formatted string ('%Y-%m-%d' or '%Y-%m-%d %H:%M:%S').
    """

    warnings.warn(
        "The format_date function is marked for deprecation in 2019, please "
        "use format_datetime instead. Note format specifiers will change (see "
        "<http://babel.pocoo.org/en/latest/dates.html#pattern-syntax>).",
        DeprecationWarning,
    )

    # Deserialize when we got a string.
    if isinstance(date, six.string_types):
        try:
            date = datetime.strptime(date, ISO_DATE_FORMAT)
        except ValueError:
            try:
                date = datetime.strptime(date, ISO_DATETIME_FORMAT)
            except ValueError as e:  # pragma: nocover
                # Exclude from code coverage as deprecated; the same code in
                # format_datetime below is covered though.
                raise TemplateException(e)

    res = date.strftime(format)
    return res


def format_datetime(date_obj, format=None, locale=None):
    """Format the specified date / date-time according to a format string.

    :param date_obj: One of: datetime.date object, datetime.datetime object,
    ISO formatted string ('%Y-%m-%d' or '%Y-%m-%d %H:%M:%S').

    :param format: How the date should be formatted. We use babel to format;
    see <http://babel.pocoo.org/en/latest/dates.html#pattern-syntax>. Optional;
    when left as is, the default format is:
    * 'YYYY-MM-dd' for datetime.date objects.
    * 'YYYY-MM-dd HH:mm:ss' for datetime.datetime objects.
    :type format: String.

    :param locale: Locale identifier used during babel formatting. Optional but
    recommended; otherwise the default system locale will be used.
    :type locale: String.

    :rtype: String.
    """

    # This is the default value in format_* functions called below.
    if locale is None:
        locale = babel.dates.LC_TIME

    # Deserialize when we got a string.
    if isinstance(date_obj, six.string_types):

        try:
            date_obj = datetime.strptime(date_obj, ISO_DATE_FORMAT)
            is_datetime = False  # This is a date (not a datetime).

        except ValueError:
            try:
                date_obj = datetime.strptime(date_obj, ISO_DATETIME_FORMAT)
                is_datetime = True  # This is a datetime (not a date).
            except ValueError as e:
                raise TemplateException(e)

    else:
        # Not a string: Find out whether we got a date or datetime.
        is_datetime = isinstance(date_obj, datetime)

    if is_datetime:
        # This is a datetime (not a date).
        if format is None:
            format = "YYYY-MM-dd HH:mm:ss"
        return babel.dates.format_datetime(
            datetime=date_obj, format=format, locale=locale
        )

    # This is a date (not a datetime).
    if format is None:
        format = "YYYY-MM-dd"
    return babel.dates.format_date(date=date_obj, format=format, locale=locale)


def format_multiline(value):
    """Allow line breaks in input data with a format function.
    Escape and replace code originally by tonthon tonthon.
    """
    value = escape(value)
    value = value.replace(u"\n", u"<text:line-break/>")
    return Markup(value)


def get_var_corresponding_ods_type(var):
    """Check variable type and return the corresponding ODS value."""
    if isinstance(var, (int, float)):
        return "float"
    return "string"


class FrameInjector(object):
    def __init__(self, template):
        """Inject a proper <draw:frame/> attributes into the template manifest
        when called back from genshi template rendering
        :param template: the py3o.template.Template instance this injector
        must work with
        :type template: py3o.template.Template instance
        """
        self.template = template

    def __call__(
        self,
        data,
        mime_type,
        width=None,
        height=None,
        isb64=False,
        keep_ratio=True,
        origin_attrib={},
        dummy=None,
    ):
        """this will be called by genshi when rendering its template

        :param data: the image data, either as a base64 encoded string or
        as the raw binary data directly from a file.read()
        :type data: string or binary data

        :param mime_type: the mime type of your image (ie: 'png', 'jpg')
        :type mime_type: string

        :param width: the desired width of your image.
        :type width: string

        :param height: the desired height of your image. (e.g. '1.4cm')
        :type height: string

        :param isb64: a flag to tell the engine your image data is not in raw
        format but an b64encode()ed version. If set to True, the engine will
        try to b64decode() your data before saving it to a file for
        LibreOffice.
        Default value is False.
        :type isb64: Boolean

        :param keep_ratio: keep the aspect ratio of the image.
        Default value is True.
        :type keep_ratio: Boolean

        :param origin_attrib: attributes of the <draw:frame/> node in the
        template file.
        :type origin_attrib: dict

        :param dummy: allows for a different name for the frame, when using
        the same image data is needed at different points on the same document.
        :type dummy: int

        :returns: a dict of attributes that can be set on the node that is
        being treated by Genshi.
        :raises: TypeError if your set the isb64 flag but your data were
        incorrectly padded or if there are non-alphabet characters
        present in the data string.
        """

        if not data:
            return {}

        if isb64:
            # we need to decode the base64 data to obtain the raw data version
            data = b64decode(data)
        if keep_ratio:
            ifile = StringIO(data)
            ifile.seek(0)
            pil_img = Image.open(ifile)
            # img_ratio = width / height
            if pil_img.size[0] and pil_img.size[1]:
                img_ratio = pil_img.size[0] / float(pil_img.size[1])
                if not (height or width):
                    # set either height or width in order to fit image to frame
                    frame_height = origin_attrib[
                        "{%s}height" % self.template.namespaces["svg"]
                    ]
                    frame_width = origin_attrib[
                        "{%s}width" % self.template.namespaces["svg"]
                    ]
                    # assume same unit for height and width. It doesn't seem
                    # possible to give different units with LibreOffice.
                    height_float = float(
                        re.sub(r"[a-zA-Z]+", "", frame_height)
                    )
                    width_float = float(re.sub(r"[a-zA-Z]+", "", frame_width))
                    frame_ratio = width_float / height_float
                    if frame_ratio > img_ratio:
                        height = frame_height
                    else:
                        width = frame_width
                if height:
                    height_float = float(re.sub(r"[a-zA-Z]+", "", height))
                    uom = re.sub(r"[\d\.]+", "", height)
                    width_float = height_float * img_ratio
                    width = "%.3f%s" % (width_float, uom)
                elif width:
                    width_float = float(re.sub(r"[a-zA-Z]+", "", width))
                    uom = re.sub(r"[\d\.]+", "", width)
                    height_float = width_float / img_ratio
                    height = "%.3f%s" % (height_float, uom)
        if width:
            origin_attrib[
                "{%s}width" % self.template.namespaces["svg"]
            ] = width

        if height:
            origin_attrib[
                "{%s}height" % self.template.namespaces["svg"]
            ] = height
        return origin_attrib


class ImageInjector(object):
    def __init__(self, template):
        """Inject an image data into the template manifest when called back
        from genshi template rendering
        :param template: the py3o.template.Template instance this injector
        must work with
        :type template: py3o.template.Template instance
        """
        self.template = template

    def __call__(
        self,
        data,
        mime_type,
        width=None,
        height=None,
        isb64=False,
        keep_ratio=True,
        dummy=None,
    ):
        """this will be called by genshi when rendering its template
        We only register our image data with a unique identifier

        :param data: the image data, either as a base64 encoded string or
        as the raw binary data directly from a file.read()
        :type data: string or binary data

        :param mime_type: the mime type of your image (ie: 'png', 'jpg')
        :type mime_type: string

        :param width: the desired width of your image.
        :type width: string

        :param height: the desired height of your image (e.g. '1.4cm').
        :type height: string

        :param isb64: a flag to tell the engine your image data is not in raw
        format but an b64encode()ed version. If set to True, the engine will
        try to b64decode() your data before saving it to a file for
        LibreOffice.
        Default value is False.
        :type isb64: Boolean

        :param keep_ratio: keep the aspect ratio of the image. Must be used
        with either the height or the width argument (using both doesn't
        make sense)
        Default value is True.
        :type keep_ratio: Boolean

        :param dummy: allows for a different name for the frame, when using
        the same image data is needed at different points on the same document.
        :type dummy: int

        :returns: a dict of attributes that can be set on the node that is
        being treated by Genshi.
        :raises: TypeError if your set the isb64 flag but your data were
        incorrectly padded or if there are non-alphabet characters
        present in the data string.
        """
        if not data:
            return {}

        if isb64:
            # we need to decode the base64 data to obtain the raw data version
            data = b64decode(data)
        identifier = "Pictures/" + hashlib.sha256(data).hexdigest()
        self.template.set_image_data(identifier, data, mime_type=mime_type)

        attrs = {
            "{%s}href" % self.template.namespaces["xlink"]: identifier,
            "{%s}type" % self.template.namespaces["xlink"]: "simple",
            "{%s}name"
            % self.template.namespaces["draw"]: ("py3o: %s" % identifier),
        }
        return attrs


class TextTemplate(object):
    """A specific template that can be used to output textual content.

    It works as the ODT or ODS templates, minus the fact that is does not
    support images.
    """

    def __init__(
        self,
        template,
        outfile,
        encoding="utf-8",
        ignore_undefined_variables=False,
    ):
        """
        :param template: a genshi text template. For more information you can
        refer to the Genshi documentation:
          http://genshi.edgewall.org/wiki/ApiDocs/genshi.template.text

        :type template: a string representing the full path name to a
        template file.

        :param outfile: the desired file name for the resulting text document
        :type outfile: a string representing the full filename for output

        :param encoding: By default the text encoding of the output will be
        UTF8. If you want another encoding you must specify it.
        :type encoding: a string representin the desired output encoding

        :param ignore_undefined_variables: Not defined variables are replaced
        with an empty string during template rendering if True
        :type ignore_undefined_variables: boolean. Default is False
        """

        self.outputfilename = outfile
        self.encoding = encoding

        content = codecs.open(template, "rb", encoding="utf-8").read()

        if ignore_undefined_variables:
            self.template = GenshiTextTemplate(content, lookup="lenient")
        else:
            self.template = GenshiTextTemplate(content)

    def render(self, data):
        """Render the template with the provided data.

        :param data: a dictionnary containing your data (preferably
        a iterators)
        :return: Nothing
        """
        with codecs.open(
            self.outputfilename, "wb+", encoding=self.encoding
        ) as outfile:

            for kind, data, pos in self.template.generate(**data):
                outfile.write(data)


class Template(object):
    """The default template to be used to output ODF content."""

    templated_files = ["content.xml", "styles.xml", MANIFEST]

    def __init__(
        self,
        template,
        outfile,
        ignore_undefined_variables=False,
        escape_false=False,
    ):
        """A template object exposes the API to render it to an OpenOffice
        document.

        @param template: a py3o template file. ie: a OpenDocument with the
        proper py3o markups
        @type template: a string representing the full path name to a py3o
        template file.

        @param outfile: the desired file name for the resulting ODT document
        @type outfile: a string representing the full filename for output

        @param ignore_undefined_variables: Not defined variables are replaced
        with an empty string during template rendering if True
        @type ignore_undefined_variables: boolean. Default is False

        @param escape_false: Values evaluated as False are replaced
        with an empty string during template rendering if True
        @type escape_false: boolean. Default is False
        """
        self.template = template
        self.outputfilename = outfile
        self.infile = zipfile.ZipFile(self.template, "r")

        self.content_trees = [
            lxml.etree.parse(BytesIO(self.infile.read(filename)))
            for filename in self.templated_files
        ]
        self.tree_roots = [tree.getroot() for tree in self.content_trees]

        self.__prepare_namespaces()

        self.images = {}
        self.output_streams = []
        self.ignore_undefined_variables = ignore_undefined_variables
        self.escape_false = escape_false

    def __prepare_namespaces(self):
        """create proper namespaces for our document
        """
        # create needed namespaces
        self.namespaces = dict(
            text="urn:text",
            draw="urn:draw",
            table="urn:table",
            office="urn:office",
            xlink="urn:xlink",
            svg="urn:svg",
            manifest="urn:manifest",
        )

        # copy namespaces from original docs
        for tree_root in self.tree_roots:
            self.namespaces.update(tree_root.nsmap)

        # remove any "root" namespace as lxml.xpath do not support them
        self.namespaces.pop(None, None)

        # declare the genshi namespace
        self.namespaces["py"] = GENSHI_URI
        # declare the regexp namespace
        self.namespaces["regexp"] = REGEXP_URI
        # declare our own namespace
        self.namespaces["py3o"] = PY3O_URI

    def get_all_user_python_expression(self):
        """  Public method to get all python expression
        """
        res = []
        text_nmspc = self.namespaces["text"]
        table_nmspc = self.namespaces["table"]
        for e in get_all_python_expression(
            self.content_trees, self.namespaces
        ):
            if e.tag == "{%s}user-field-get" % text_nmspc:
                py_expr = e.get("{%s}name" % text_nmspc)
                # Remove the trailing 'py3o.'
                res.append(py_expr[5:])
            elif e.tag == "{%s}a" % text_nmspc:
                py_expr = e.get("{%s}href" % self.namespaces["xlink"])
                # Remove the trailing 'py3o://'
                # Also convert the url string into a classic string
                res.append(urllib.parse.unquote(py_expr[7:]))
            elif e.tag == "{%s}p" % text_nmspc:
                if e.text:
                    res.extend(re.findall(r"\${([^{}]*)}", e.text))
            elif e.tag == "{%s}table-cell" % table_nmspc:
                formula = e.get("{%s}formula" % table_nmspc)
                res.extend(re.findall(r"\${([^{}]*)}", formula))
        return res

    def get_user_instructions(self):
        """ Public method to help report engine to find all instructions
        This method will be removed in a future version.
        Please use :meth:`.Py3oTemplate.get_all_user_python_expression`.
        """
        warnings.warn(
            "This method will be removed in a future version. "
            "Please use get_all_user_python_expression() instead.",
            DeprecationWarning,
        )
        res = []
        # TODO: Check if instructions can be stored in other content_trees
        for e in get_instructions(self.content_trees[0], self.namespaces):
            childs = e.getchildren()
            if childs:
                res.extend([c.text for c in childs])
            else:
                res.append(e.text)
        return res

    def get_user_variables(self):
        """a public method to help report engines to introspect
        a template and find what data it needs and how it will be
        used
        returns a list of user variable names without the leading 'py3o.'
        This method will be removed in a future version.
        Please use :meth:`.Py3oTemplate.get_all_user_python_expression`.
        """
        # TODO: Check if some user fields are stored in other content_trees
        warnings.warn(
            "This method will be removed in a future version. "
            "Please use get_all_user_python_expression() instead.",
            DeprecationWarning,
        )
        return [
            e.get("{%s}name" % e.nsmap.get("text"))[5:]
            for e in get_user_fields(self.content_trees[0], self.namespaces)
        ]

    def remove_soft_breaks(self):
        for soft_break in get_soft_breaks(
            self.content_trees[0], self.namespaces
        ):
            parent = soft_break.getparent()
            if soft_break.tail:
                if parent.text:
                    parent.text += soft_break.tail
                else:
                    parent.text = soft_break.tail
            parent.remove(soft_break)

    @staticmethod
    def convert_py3o_to_python_ast(expressions):
        """Convert py3o expressions to parsable Python code.

        The py3o expressions can be extracted from a Template object using
        the :meth:`get_all_user_python_expression` method.
        The result can then be parsed by :class:`Py3oConvertor` in order to
        obtain the data structure expected by the template.

        :param list expressions:
          A list of strings that represent expressions in the template.

        :returns:
          The expressions in the form of Python code that can be parsed by AST.
        :rtype: str
        """
        python_src = ""
        indent = 0

        def pindent():
            # Easily add indentation
            return indent * " "

        for expression in expressions:
            if expression.startswith("for="):
                # For loop
                # We construct a python for loop with the py3o one
                python_src += "{}for {}:\n".format(pindent(), expression[5:-1])
                indent += 1
                # Care of empty loop statement
                if expressions[expressions.index(expression) + 1] == "/for":
                    python_src += "{}pass\n".format(pindent())
            elif expression == "/for":
                # End of for loop
                indent -= 1
            elif expression.startswith("if="):
                # Construct an if statement
                python_src += "{}if {}:\n".format(pindent(), expression[4:-1])
                indent += 1
                # Care of empty if statement
                if expressions[expressions.index(expression) + 1] == "/if":
                    python_src += "{}pass\n".format(pindent())
            elif expression == "/if":
                # End of if
                indent -= 1
            elif expression.startswith("function="):
                # Convert to a function call
                python_src += "{}{}\n".format(pindent(), expression[10:-1])
            else:
                # Variable access
                python_src += "{}{}\n".format(pindent(), expression)
        return python_src

    @staticmethod
    def find_image_frames(content_trees, namespaces):
        """find all frames that must be converted to images
        """
        tags = []

        for content_tree in content_trees:
            for frame in get_image_frames(content_tree, namespaces):
                py3o_statement = urllib.parse.unquote(
                    frame.attrib["{%s}name" % namespaces["draw"]]
                )
                # remove the "py3o.image("
                py3o_base = py3o_statement[11:]
                # remove the trailing ")"
                py3o_base = py3o_base[:-1]

                tags.append((frame, py3o_base))

        return tags

    @staticmethod
    def find_instructions(content_trees, namespaces):

        opened_starts = list()
        starting_tags = list()
        closing_tags = dict()

        attrib_xlink = "{%s}href" % namespaces["xlink"]
        attrib_text = "{%s}description" % namespaces["text"]

        for content_tree in content_trees:
            for link in get_instructions(content_tree, namespaces):
                if attrib_xlink in link.attrib:
                    py3o_statement = urllib.parse.unquote(
                        link.attrib[attrib_xlink]
                    )
                elif attrib_text in link.attrib:
                    py3o_statement = urllib.parse.unquote(
                        link.attrib[attrib_text]
                    )
                else:
                    raise NotImplementedError
                # remove the py3o://
                py3o_base = py3o_statement[7:]

                if not py3o_base.startswith("/"):
                    if not py3o_base.startswith("function"):
                        opened_starts.append(link)
                    starting_tags.append((link, py3o_base))

                else:
                    if not opened_starts:
                        raise TemplateException(
                            "No open instruction for %s" % py3o_base
                        )

                    closing_tags[id(opened_starts.pop())] = link

        return starting_tags, closing_tags

    def apply_variable_type_in_cells(self, content_trees, namespaces):
        """Replace default 'string' type by a function call."""
        text_nmspc = namespaces["text"]
        for e in get_all_python_expression(content_trees, namespaces):
            if e.tag == "{%s}p" % text_nmspc:
                if not e.text:
                    continue
                parent = e.getparent()
                varname = re.findall(r"\${([^{}]*)}", e.text)[0]
                for ns in ("office", "calcext"):
                    parent.attrib["{%s}value-type" % namespaces[ns]] = (
                        "${get_var_corresponding_ods_type(%s)}" % varname
                    )
                parent.attrib["{%s}value" % namespaces["office"]] = (
                    "${%s}" % varname
                )

    @staticmethod
    def validate_link(link, py3o_base):
        """this method will ensure a link is valid or raise a TemplateException

        :param link: a link node found in the tree
        :type link: lxml.Element

        :returns: nothing
        :raises: TemplateException
        """
        # Don't enfoce on text-input fields
        if link.tag.endswith("text-input"):
            return
        # OLD open office version
        if link.text is not None and link.text.strip():
            if not link.text == py3o_base:
                msg = "url and text do not match in '%s'" % link.text
                raise TemplateException(msg)

        # new open office version
        elif len(link):
            if not link[0].text == py3o_base:
                msg = "url and text do not match in '%s'" % link[0].text
                raise TemplateException(msg)
        else:
            msg = "Text not found for link '%s'" % link.attrib
            raise TemplateException(msg)

    def handle_draw_frame(self, frame, py3o_base):
        """remove a draw:frame content and inject a draw:image with
        py:attrs="__py3o_image(image_name)"
        this __py3o_image method will be injected inside the template
        dictionary to be called back from inside the template
        """
        image_inserter = "__py3o_image(%s)" % py3o_base
        frame_args = (
            py3o_base + six.u(", origin_attrib=") + six.text_type(frame.attrib)
        )
        frame_inserter = "__py3o_frame(%s)" % frame_args
        attrib_image = {"{%s}attrs" % self.namespaces["py"]: image_inserter}
        attrib_frame = {"{%s}attrs" % self.namespaces["py"]: frame_inserter}
        nsmap = {"draw": self.namespaces["draw"], "py": GENSHI_URI}
        drawframe = lxml.etree.Element(
            "{%s}frame" % self.namespaces["draw"],
            attrib=attrib_frame,
            nsmap=nsmap,
        )
        lxml.etree.SubElement(
            drawframe,
            "{%s}image" % self.namespaces["draw"],
            attrib=attrib_image,
            nsmap=nsmap,
        )
        # first child in the frame (ie: draw:text-box or equivalent), will be
        # removed and replaced by our new draw:image node we created
        frame.getparent().replace(frame, drawframe)

    def handle_link(self, link, py3o_base, closing_link):
        """transform a py3o link into a proper Genshi statement
        rebase a py3o link at a proper place in the tree
        to be ready for Genshi replacement
        """
        self.validate_link(link, py3o_base)

        # find out if the instruction is inside a table
        parent = link.getparent()
        keep_start_boundary = False
        keep_end_boundary = False

        # keep the link's previous node style
        # if we need to apply its style later
        previous_node = link.getprevious()

        if parent.getparent() is not None and parent.getparent().tag == (
            "{%s}table-cell" % self.namespaces["table"]
        ):
            # we are in a table
            opening_paragraph = parent
            opening_cell = opening_paragraph.getparent()

            # same for closing
            if closing_link is not None:
                closing_paragraph = closing_link.getparent()
                closing_cell = closing_paragraph.getparent()
                if opening_cell == closing_cell:
                    # block is fully in a single cell
                    opening_row = opening_paragraph
                    closing_row = closing_paragraph
                else:
                    opening_row = opening_cell.getparent()
                    closing_row = closing_cell.getparent()
            else:
                opening_row = opening_paragraph

        elif (
            parent.tag == "{%s}p" % self.namespaces["text"]
            or parent.tag == "{%s}span" % self.namespaces["text"]
        ):
            # if we are using text we want to keep start/end nodes
            keep_start_boundary, keep_end_boundary = detect_keep_boundary(
                link, closing_link, self.namespaces
            )
            # we are in a text paragraph
            opening_row = parent
            closing_row = (
                closing_link.getparent() if closing_link is not None else None
            )

        else:  # pragma: no cover
            raise NotImplementedError(
                "We handle urls in tables or text paragraph only "
                "(url: %s)" % py3o_base
            )

        # max split is one
        try:
            instruction, instruction_value = py3o_base.split("=", 1)
        except Exception:
            raise TemplateException(
                "Missing '=' in instruction '%s'" % py3o_base
            )
        instruction_value = instruction_value.strip('"')

        # Handle function call
        if instruction == "function":
            instruction = "content"

        attribs = dict()
        attribs["{%s}strip" % GENSHI_URI] = "True"
        attribs["{%s}%s" % (GENSHI_URI, instruction)] = instruction_value

        genshi_node = lxml.etree.Element(
            "span", attrib=attribs, nsmap={"py": GENSHI_URI}
        )

        link.getparent().remove(link)
        if closing_link is not None:
            closing_link.getparent().remove(closing_link)

        if instruction == "content":
            # Find the previous node style
            style_node = previous_node if previous_node is not None else parent

            # Create a span
            new_span = lxml.etree.Element(
                "{%s}span" % self.namespaces["text"],
                attrib={
                    "{%s}style-name"
                    % self.namespaces["text"]: style_node.get(
                        "{%s}style-name" % self.namespaces["text"]
                    )
                },
            )
            # Put the span at the same place the link was
            new_span.append(genshi_node)
            opening_row.append(new_span)
        else:
            try:
                move_siblings(
                    opening_row,
                    closing_row,
                    genshi_node,
                    keep_start_boundary=keep_start_boundary,
                    keep_end_boundary=keep_end_boundary,
                )
            except ValueError:  # pragma: no cover
                excrepr = traceback.format_exc()
                log.exception(excrepr)
                raise TemplateException(
                    "Could not move siblings for '%s'" % py3o_base
                )

    def __prepare_userfield_decl(self):
        self.field_info = dict()

        for content_tree in self.content_trees:
            # here we gather the fields info in one pass to be able to avoid
            # doing the same operation multiple times.
            for userfield in get_user_fields(content_tree, self.namespaces):

                value = userfield.attrib["{%s}name" % self.namespaces["text"]][
                    5:
                ]

                value_type = userfield.attrib.get(
                    "{%s}value-type" % self.namespaces["office"], "string"
                )

                value_datastyle_name = userfield.attrib.get(
                    "{%s}data-style-name" % self.namespaces["style"]
                )

                self.field_info[value] = {
                    "name": value,
                    "value_type": value_type,
                    "value_datastyle_name": value_datastyle_name,
                }

    def __prepare_calc_formulas(self):
        """Prepare simple Genshi expressions used inside ODS cell formulas.

        This method searches inside formulas for every Genshi expression that
        only consists of a name or attribute access. Any such expression
        ``my_odf_value`` will be replaced in the formula with::

            VALUE(${getattr(my_odf_value, "odf_value", odf_value)})

        Note that any double quote placed immediately before or after the
        Genshi expression will be automatically removed.

        Therefore, the preferred way to render a piece of data using the
        formatting defined for the ODS cell is simply::

            ="${my_ODF_value}"
        """

        field_expr = (
            r"//table:table-cell[regexp:match(@table:formula, '\${[^\${}]*}')]"
        )

        for content_tree in self.content_trees:

            for userfield in content_tree.xpath(
                field_expr, namespaces=self.namespaces
            ):
                formula_attr = "{%s}formula" % self.namespaces["table"]
                value = userfield.attrib[formula_attr]
                userfield.attrib[formula_attr] = re.sub(
                    r"\"?\${([\w.]*?)(?<!odf_value)}\"?",
                    r"VALUE(${\1 if isinstance(\1, (int, float)) "
                    r'else getattr(\1, "odf_value", "\"{}\"".format(\1))})',
                    value,
                )

    def __prepare_usertexts(self):
        """Replace user-type text fields that start with "py3o." with genshi
        instructions.
        """

        field_expr = r"//text:user-field-get[starts-with(@text:name, 'py3o.')]"

        for content_tree in self.content_trees:

            for userfield in content_tree.xpath(
                field_expr, namespaces=self.namespaces
            ):
                parent = userfield.getparent()
                value = userfield.attrib["{%s}name" % self.namespaces["text"]][
                    5:
                ]
                style_attr = "{%s}data-style-name" % self.namespaces["style"]
                style = userfield.attrib.get(style_attr)
                if_attr = "{%s}if" % self.namespaces["py"]

                attribs = dict()
                attribs["{%s}strip" % GENSHI_URI] = "True"
                attribs["{%s}content" % GENSHI_URI] = value

                if self.escape_false:
                    attribs[if_attr] = value

                if style is not None:
                    node_tag = "{%s}expression" % self.namespaces["text"]

                    formula = (
                        "ooow:VALUE(\"${{getattr({val}, '{key}', '')}}\")"
                    ).format(val=value, key="odf_value")
                    vtype = "${{getattr({val}, '{key}', '{default}')}}".format(
                        val=value, key="odf_type", default="string"
                    )
                    if_condition = "hasattr({val}, '{key}')".format(
                        val=value, key="odf_value"
                    )

                    formula_attribs = {
                        "{%s}content" % GENSHI_URI: value,
                        style_attr: style,
                        if_attr: if_condition,
                        "{%s}formula" % self.namespaces["text"]: formula,
                        "{%s}value-type" % self.namespaces["office"]: vtype,
                    }
                    formula_node = lxml.etree.Element(
                        node_tag, attrib=formula_attribs, nsmap=self.namespaces
                    )
                    userfield.addprevious(formula_node)

                    attribs[if_attr] = "not {cond}".format(cond=if_condition)

                genshi_node = lxml.etree.Element(
                    "span", attrib=attribs, nsmap={"py": GENSHI_URI}
                )

                if userfield.tail:
                    genshi_node.tail = userfield.tail

                parent.replace(userfield, genshi_node)

    def __replace_image_links(self):
        """Replace links of placeholder images (the name of which starts with
        "py3o.staticimage.") to point to a file saved the "Pictures"
        directory of the archive.
        """

        image_expr = (
            "//draw:frame[starts-with(@draw:name, 'py3o.staticimage')]"
        )

        for content_tree in self.content_trees:

            # Find draw:frame tags.
            for draw_frame in content_tree.xpath(
                image_expr, namespaces=self.namespaces
            ):
                # Find the identifier of the image
                # (py3o.staticimage[identifier]).
                image_id = draw_frame.attrib[
                    "{%s}name" % self.namespaces["draw"]
                ][5:]
                if image_id not in self.images:
                    if not self.ignore_undefined_variables:
                        raise TemplateException(
                            "Can't find data for the image named 'py3o.%s'; "
                            "make sure it has been added with the "
                            "set_image_path or set_image_data methods."
                            % image_id
                        )

                # Replace the xlink:href attribute of the image to point to
                # ours.
                image = draw_frame[0]
                image.attrib["{%s}href" % self.namespaces["xlink"]] = image_id

    def __add_images_to_manifest(self):
        """Add entries for py3o images into the manifest file."""

        xpath_expr = "//manifest:manifest[1]"

        for content_tree in self.content_trees:

            # Find manifest:manifest tags.
            manifest_e = content_tree.xpath(
                xpath_expr, namespaces=self.namespaces
            )
            if not manifest_e:
                continue

            for identifier in self.images.keys():
                mime = self.images.get(identifier).get("mime_type", None)
                attribs = {
                    "{%s}full-path" % self.namespaces["manifest"]: identifier,
                    "{%s}media-type" % self.namespaces["manifest"]: mime or "",
                }
                # Add a manifest:file-entry tag.
                lxml.etree.SubElement(
                    manifest_e[0],
                    "{%s}file-entry" % self.namespaces["manifest"],
                    attrib=attribs,
                )
            return manifest_e[0]

    def add_base_data_to_template(self):
        return {
            "decimal": decimal,
            "format_amount": format_amount,  # deprecated -> format_currency
            "format_currency": format_currency,
            "format_locale": format_locale,  # deprecated -> format_currency
            "format_date": format_date,  # deprecated -> format_datetime
            "format_datetime": format_datetime,
            "format_multiline": format_multiline,
            "__py3o_image": ImageInjector(self),
            "__py3o_frame": FrameInjector(self),
            "get_var_corresponding_ods_type": get_var_corresponding_ods_type,
        }

    def render_tree(self, data):
        """prepare the flows without saving to file
        this method has been decoupled from render_flow to allow better
        unit testing
        """

        # Soft page breaks are hints for applications for rendering a page
        # break. Soft page breaks in for loops may compromise the paragraph
        # formatting especially the margins. Open-/LibreOffice will regenerate
        # the page breaks when displaying the document. Therefore it is safe to
        # remove them.
        self.remove_soft_breaks()

        # first we need to transform the py3o template into a valid
        # Genshi template.
        starting_tags, closing_tags = self.find_instructions(
            self.content_trees, self.namespaces
        )
        parent2tag = {}  # key = parent ; value = tag
        for tag in starting_tags:
            parent = tag[0].getparent()
            if parent in parent2tag:
                raise TemplateException(
                    "Every py3o link instruction should be on its own line. "
                    "Two py3o link instructions are on the same line: "
                    "<%s> and <%s>" % (tag[1], parent2tag[parent][1])
                )
            else:
                parent2tag[parent] = tag

        for link, py3o_base in starting_tags:
            self.handle_link(link, py3o_base, closing_tags.get(id(link), None))

        # handle all draw links that will need to receive image content
        # in their childrens
        tags = self.find_image_frames(self.content_trees, self.namespaces)
        # draw frames with special names will be auto injected with image
        # injectors
        for frame, py3o_base in tags:
            self.handle_draw_frame(frame, py3o_base)

        # check variable types and apply them to the resulting doc
        self.apply_variable_type_in_cells(self.content_trees, self.namespaces)

        self.__prepare_userfield_decl()
        self.__prepare_usertexts()
        self.__prepare_calc_formulas()

        self.__replace_image_links()

        # Add base functions/module access inside the template.
        # Also allow users to add their own data
        new_data = self.add_base_data_to_template()

        for fnum, content_tree in enumerate(self.content_trees):
            content = lxml.etree.tostring(content_tree.getroot())
            if self.ignore_undefined_variables:
                template = MarkupTemplate(content, lookup="lenient")
            else:
                template = MarkupTemplate(content)

            # then we need to render the genshi template itself by
            # providing the data to genshi

            template_dict = {}
            template_dict.update(data.items())
            template_dict.update(new_data.items())

            self.output_streams.append(
                (
                    self.templated_files[fnum],
                    template.generate(**template_dict),
                )
            )

    def render_flow(self, data):
        """render the OpenDocument with the user data

        @param data: the input stream of user data. This should be a dictionary
        mapping, keys being the values accessible to your report.
        @type data: dictionary
        """

        self.render_tree(data)

        # then reconstruct a new ODT document with the generated content
        for status in self.__save_output():
            yield status

    def render(self, data):
        """render the OpenDocument with the user data

        @param data: the input stream of userdata. This should be a dictionary
        mapping, keys being the values accessible to your report.
        @type data: dictionary
        """
        for status in self.render_flow(data):
            if not status:  # pragma: no cover
                raise TemplateException("unknown template error")

    def set_image_path(self, identifier, path):
        """Set data for an image mentioned in the template.

        @param identifier: Identifier of the image; refer to the image in the
        template by setting "py3o.[identifier]" as the name of that image.
        @type identifier: string

        @param path: Image path on the file system
        @type path: string
        """

        f = open(path, "rb")
        self.set_image_data(identifier, f.read())
        f.close()

    def set_image_data(self, identifier, data, mime_type=None):
        """Set data for an image mentioned in the template.

        @param identifier: Identifier of the image; refer to the image in the
        template by setting "py3o.staticimage.[identifier]" as the name
        of that image.
        @type identifier: string

        @param data: Contents of the image.
        @type data: binary
        """

        self.images[identifier] = {"data": data, "mime_type": mime_type}

    def __save_output(self):
        """Saves the output into a native OOo document format.
        """
        out = zipfile.ZipFile(self.outputfilename, "w", allowZip64=True)

        manifest_info = None
        for info_zip in self.infile.infolist():
            if "manifest.xml" in info_zip.filename:
                manifest_info = info_zip
                continue

            if info_zip.filename in self.templated_files:
                # get a temp file
                streamout = open(get_secure_filename(), "w+b")

                # Template file - we have edited these.
                fname, output_stream = self.output_streams[
                    self.templated_files.index(info_zip.filename)
                ]

                transformer = get_list_transformer(self.namespaces)
                nstream = output_stream | transformer

                # write the whole stream to it
                for chunk in nstream.serialize():
                    streamout.write(chunk.encode("utf-8"))
                    yield True

                streamout.seek(0)

                # close the temp file to flush all data and make sure we get
                # it back when writing to the zip archive.
                streamout.close()

                # write the full file to archive
                out.write(streamout.name, fname)

                # remove temp file
                os.unlink(streamout.name)

            else:
                # Copy other files straight from the source archive.
                out.writestr(info_zip, self.infile.read(info_zip.filename))

        # the manifest must be processed at the end since its content
        # depends on the processing of others files (ie: content.xml)
        if manifest_info:
            manifest_e = self.__add_images_to_manifest()
            out.writestr(manifest_info, lxml.etree.tostring(manifest_e))

        # Save images in the "Pictures" sub-directory of the archive.
        for identifier, im_struct in self.images.items():
            out.writestr(identifier, im_struct.get("data"))

        # close the zipfile before leaving
        out.close()
        yield True
