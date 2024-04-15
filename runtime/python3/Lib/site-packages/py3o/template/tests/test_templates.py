# -*- encoding: utf-8 -*-
import datetime
import os
import re
import unittest
import zipfile
import traceback
import copy
import base64

import lxml.etree
import pkg_resources
import six

from io import BytesIO

from genshi.template import TemplateError
from PIL import Image
from pyjon.utils import get_secure_filename

from py3o.template import Template, TextTemplate, TemplateException
from py3o.template.main import (
    XML_NS,
    get_image_frames,
    get_soft_breaks,
    MANIFEST,
)

if six.PY3:
    # noinspection PyUnresolvedReferences
    from unittest.mock import Mock
elif six.PY2:
    # noinspection PyUnresolvedReferences
    from mock import Mock


class TestTemplate(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_example_1(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_example_template.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)
        template.set_image_path(
            "staticimage.logo",
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/images/new_logo.png"
            ),
        )

        class Item(object):
            pass

        items = list()

        item1 = Item()
        item1.val1 = "Item1 Value1"
        item1.val2 = "Item1 Value2"
        item1.val3 = "Item1 Value3"
        item1.Currency = "EUR"
        item1.Amount = "12345.35"
        item1.InvoiceRef = "#1234"
        items.append(item1)

        # if you are using python 2.x you should use xrange
        for i in range(1000):
            item = Item()
            item.val1 = "Item%s Value1" % i
            item.val2 = "Item%s Value2" % i
            item.val3 = "Item%s Value3" % i
            item.Currency = "EUR"
            item.Amount = "6666.77"
            item.InvoiceRef = "Reference #%04d" % i
            items.append(item)

        document = Item()
        document.total = "9999999999999.999"

        data = dict(items=items, document=document)
        error = False
        try:
            template.render(data)
        except ValueError:
            print("The template did not render properly...")
            traceback.print_exc()
            error = True

        assert error is False

    def test_link_validation_missing_equal(self):
        """test a missing equal sign in a link raises a template error"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_missing_eq_in_link.odt"
        )
        outname = get_secure_filename()

        template = Template(template_name, outname)

        class Item(object):
            def __init__(self, val):
                self.val = val

        data_dict = {"items": [Item(1), Item(2), Item(3), Item(4)]}

        template.set_image_path(
            "staticimage.logo",
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/images/new_logo.png"
            ),
        )
        except_occured = False
        error_text = ""
        try:
            template.render(data_dict)
        except TemplateException as e:
            except_occured = True
            error_text = "{}".format(e)

        assert except_occured is True
        assert error_text == (
            "Missing '=' in instruction 'for \"item in items\"'"
        )

    def test_list_duplicate(self):
        """test duplicated listed get a unique id"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_list_template.odt"
        )
        outname = get_secure_filename()

        template = Template(template_name, outname)

        class Item(object):
            def __init__(self, val):
                self.val = val

        data_dict = {"items": [Item(1), Item(2), Item(3), Item(4)]}

        error = False

        template.set_image_path(
            "staticimage.logo",
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/images/new_logo.png"
            ),
        )
        template.render(data_dict)

        outodt = zipfile.ZipFile(outname, "r")
        try:
            content_list = [
                lxml.etree.parse(BytesIO(outodt.read(filename)))
                for filename in template.templated_files
            ]
        except lxml.etree.XMLSyntaxError as e:
            error = True
            print("List was not deduplicated->{}".format(e))

        # remove end file
        os.unlink(outname)

        assert error is False

        # first content is the content.xml
        content = content_list[0]
        list_expr = "//text:list"
        list_items = content.xpath(list_expr, namespaces=template.namespaces)
        ids = []
        for list_item in list_items:
            ids.append(list_item.get("{}id".format(XML_NS)))
        assert ids, "this list of ids should not be empty"
        assert len(ids) == len(set(ids)), "all ids should have been unique"

    def test_missing_opening(self):
        """test orphaned /for raises a TemplateException"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_missing_open_template.odt"
        )
        outname = get_secure_filename()
        try:
            template = Template(template_name, outname)

        finally:
            os.remove(outname)

        class Item(object):
            def __init__(self, val):
                self.val = val

        data_dict = {"items": [Item(1), Item(2), Item(3), Item(4)]}

        template.set_image_path(
            "staticimage.logo",
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/images/new_logo.png"
            ),
        )
        # this will raise a TemplateException... or the test will fail
        error_occured = False
        try:
            template.render(data_dict)

        except TemplateException as e:
            error_occured = True
            # make sure this is the correct TemplateException that pops
            assert e.message == "No open instruction for /for"

        # and make sure we raised
        assert error_occured is True

    def test_ignore_undefined_variables_logo(self):

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_logo.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data = {}

        error = True
        try:
            template.render(data)
            print(
                "Error: template contains a logo variable that must be "
                "replaced"
            )
        except ValueError:
            error = False

        assert error is False

        template = Template(
            template_name, outname, ignore_undefined_variables=True
        )

        error = False
        try:
            template.render(data)
        except Exception:
            traceback.print_exc()
            error = True

        assert error is False

    def test_ignore_undefined_variables_1(self):

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_undefined_variables_1.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data = {}

        error = True
        try:
            template.render(data)
            print(
                "Error: template contains variables that must be " "replaced"
            )
        except TemplateError:
            error = False

        assert error is False

        template = Template(
            template_name, outname, ignore_undefined_variables=True
        )

        error = False
        try:
            template.render(data)
        except Exception:
            traceback.print_exc()
            error = True

        assert error is False

    def test_ignore_undefined_variables_2(self):
        """
        Test ignore undefined variables for template with dotted variables like
        py3o.document.value
        """

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_undefined_variables_2.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data = {}

        error = True
        try:
            template.render(data)
            print(
                "Error: template contains variables that must be " "replaced"
            )
        except TemplateError:
            error = False

        assert error is False

        template = Template(
            template_name, outname, ignore_undefined_variables=True
        )

        error = True
        try:
            template.render(data)
            print(
                "Error: template contains dotted variables that must be "
                "replaced"
            )
        except TemplateError:
            error = False

        assert error is False

    def test_escape_false_template(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/test_false_value.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)
        template.render({"false_value": False})
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_test_false_value_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        self.assertEqual(result_a, result_e)

        outname = get_secure_filename()

        template = Template(template_name, outname, escape_false=True)
        template.render({"false_value": False})
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_test_escape_false_value_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        self.assertEqual(result_a, result_e)

    def test_invalid_template_1(self):
        """a template should not try to define a /for and a for on the same
        paragraph
        """

        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_example_invalid_template.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        class Item(object):
            pass

        items = list()

        item1 = Item()
        item1.val1 = "Item1 Value1"
        item1.val2 = "Item1 Value2"
        item1.val3 = "Item1 Value3"
        item1.Currency = "EUR"
        item1.Amount = "12345.35"
        item1.InvoiceRef = "#1234"
        items.append(item1)

        # if you are using python 2.x you should use xrange
        for i in range(1000):
            item = Item()
            item.val1 = "Item%s Value1" % i
            item.val2 = "Item%s Value2" % i
            item.val3 = "Item%s Value3" % i
            item.Currency = "EUR"
            item.Amount = "6666.77"
            item.InvoiceRef = "Reference #%04d" % i
            items.append(item)

        document = Item()
        document.total = "9999999999999.999"

        data = dict(items=items, items2=copy.copy(items), document=document)

        error = False
        try:
            template.render(data)
        except TemplateException:
            error = True

        assert error is True, "This template should have been refused"

    def test_template_with_function_call(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_template_function_call.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"amount": 32.123}

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_with_function_call_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_format_currency(self):
        """Test py3o.template.main.format_currency which relies on babel.
        """

        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_format_currency.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {
            "zero": 0,
            "zero_float": 0.0,
            "one": 1,
            "poor": 42.42,
            "rich": 123456789.4242,
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_format_currency_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        self.assertEqual(result_a, result_e)

    def test_format_date(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_template_format_date.odt"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {
            "datestring": "2015-08-02",
            "datetimestring": "2015-08-02 17:05:06",
            "datestring2": "2015-10-15",
            "datetime": datetime.datetime.strptime(
                "2015-11-13 17:00:20", "%Y-%m-%d %H:%M:%S"
            ),
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_format_date_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_format_datetime(self):
        """Test py3o.template.main.format_datetime which relies on babel.
        """

        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_format_datetime.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {
            "datestring": "2015-08-02",
            "datetimestring": "2015-08-02 17:05:06",
            "datestring2": "2015-10-15",
            "datetime_obj": datetime.datetime.strptime(
                "2015-11-13 17:00:20", "%Y-%m-%d %H:%M:%S"
            ),
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_format_datetime_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        self.assertEqual(result_a, result_e)

    def test_format_date_exception(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_format_date_exception.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"date_obj": "2015/08/02"}

        # this will raise a TemplateException... or the test will fail
        error_occured = False
        try:
            template.render(data_dict)

        except TemplateException:
            error_occured = True

        # and make sure we raised
        assert error_occured is True

    def test_style_application_with_function_call(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/style_application_with_function_call.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"date": "2015-08-02"}

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                (
                    "tests/templates/"
                    "style_application_with_function_call_result.xml"
                ),
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_image_injection(self):
        """Test insertion of images from the data source into the template"""

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_image_injection.odt"
        )
        logo_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/images/new_logo.png"
        )
        image_names = [
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/images/image{i}.png".format(i=i),
            )
            for i in range(1, 4)
        ]
        outname = get_secure_filename()

        template = Template(template_name, outname)
        logo = open(logo_name, "rb").read()
        images = [open(iname, "rb").read() for iname in image_names]

        data_dict = {
            "items": [
                Mock(val1=i, val3=i ** 2, image=base64.b64encode(image))
                for i, image in enumerate(images, start=1)
            ],
            "document": Mock(total=6),
            "logo": logo,
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )
        namelist = outodt.namelist()

        i = 0
        nmspc = template.namespaces
        table = content_list.find("//table:table", nmspc)
        frame_path = "table:table-cell/text:p/draw:frame"
        images_hrefs = set()
        for row in table.findall("table:table-row", nmspc):

            frame_elem = row.find(frame_path, nmspc)
            if frame_elem is None:
                continue
            image_elem = frame_elem.find("draw:image", nmspc)
            self.assertIsNotNone(image_elem)

            href = image_elem.get("{{{}}}href".format(nmspc["xlink"]))
            self.assertTrue(href)
            self.assertIn(href, namelist)
            self.assertEqual(images[i], outodt.read(href))

            frame_elem.remove(image_elem)
            images_hrefs.add(href)
            i += 1

        self.assertEqual(i, 3, u"Images were not found in the output")

        # check if images are into the manifest
        manifest_el = lxml.etree.parse(BytesIO(outodt.read(MANIFEST)))
        file_entries = manifest_el.findall("//manifest:file-entry", nmspc)
        for entry in file_entries:
            path = entry.get("{{{}}}full-path".format(nmspc["manifest"]))
            if path in images_hrefs:
                images_hrefs.remove(path)
        self.assertFalse(
            images_hrefs, "All images should be into the manifest"
        )

    def test_image_injection_twice(self):
        """
        Test insertion of the same image from the data source
        at least twice into the template
        """

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_image_injection_twice.odt"
        )
        logo_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/images/new_logo.png"
        )
        image_names = [
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/images/image{i}.png".format(i=i),
            )
            for i in range(1, 4)
        ]
        outname = get_secure_filename()

        template = Template(template_name, outname)
        logo = open(logo_name, "rb").read()
        images = [open(iname, "rb").read() for iname in image_names]

        data_dict = {
            "items": [
                Mock(val1=i, val3=i ** 2, image=base64.b64encode(image))
                for i, image in enumerate(images, start=1)
            ],
            "document": Mock(total=6),
            "logo": logo,
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        list_expr = "//draw:frame"
        list_items = content_list.xpath(
            list_expr, namespaces=template.namespaces
        )
        ids = []
        for list_item in list_items:
            ids.append(list_item.get("{}id".format(XML_NS)))
        assert ids, "this list of ids should not be empty"
        assert len(ids) == len(set(ids)), "all ids should have been unique"

    def test_ignore_undefined_variables_image_injection(self):
        """Test ignore undefined variables for injected image"""

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_image_injection.odt"
        )

        outname = get_secure_filename()

        data = {"items": [], "document": Mock(total=6)}

        template = Template(template_name, outname)
        error = True
        try:
            template.render(data)
            print(
                "Error: template contains variables that must be " "replaced"
            )
        except TemplateError:
            error = False

        self.assertFalse(error)

        template = Template(
            template_name, outname, ignore_undefined_variables=True
        )
        error = False
        try:
            template.render(data)
        except Exception:
            traceback.print_exc()
            error = True

        self.assertFalse(error)

    def test_image_keep_ratio(self):
        """Test keep_ratio parameter with insertion of images"""

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_image_keep_ratio.odt"
        )

        image_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/images/new_logo.png"
        )
        image = open(image_name, "rb").read()
        pil_img = Image.open(BytesIO(image))
        img_ratio = pil_img.size[0] / float(pil_img.size[1])

        outname = get_secure_filename()

        template = Template(template_name, outname)
        nmspc = template.namespaces
        image_frames = {
            elem.get("{%s}name" % nmspc["draw"]): elem
            for elem in get_image_frames(template.content_trees[0], nmspc)
        }

        data_dict = {"image": base64.b64encode(image)}
        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")
        image_entries = get_image_frames(
            lxml.etree.parse(
                BytesIO(outodt.read(template.templated_files[0]))
            ),
            nmspc,
        )

        for frame in image_entries:
            name = frame.get("{%s}name" % nmspc["draw"])
            tframe = image_frames[name]
            if "keep_ratio=False" in name:
                # result dimension should equal template
                for dim in ["width", "height"]:
                    self.assertEqual(
                        frame.get("{%s}%s" % (nmspc["svg"], dim)),
                        tframe.get("{%s}%s" % (nmspc["svg"], dim)),
                    )
            else:
                # Compare frame aspect ratio with that of image and check that
                # frame dimensions do not exceed those of the placeholders
                height = float(
                    re.sub(
                        "[a-zA-Z]+", "", frame.get("{%s}height" % nmspc["svg"])
                    )
                )
                width = float(
                    re.sub(
                        "[a-zA-Z]+", "", frame.get("{%s}width" % nmspc["svg"])
                    )
                )
                frame_ratio = width / height
                self.assertAlmostEqual(frame_ratio, img_ratio)

                theight = float(
                    re.sub(
                        "[a-zA-Z]+",
                        "",
                        tframe.get("{%s}height" % nmspc["svg"]),
                    )
                )
                twidth = float(
                    re.sub(
                        "[a-zA-Z]+", "", tframe.get("{%s}width" % nmspc["svg"])
                    )
                )
                self.assertLessEqual(height, theight)
                self.assertLessEqual(width, twidth)

    def test_text_template(self):

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_text_template"
        )

        user_data = {
            "mylist": [
                Mock(var0=1, var1="1", var2=1.0),
                Mock(var0=2, var1="2", var2=2.0),
                Mock(var0=3, var1="3", var2=3.0),
            ]
        }

        outname = get_secure_filename()

        template = TextTemplate(template_name, outname)
        template.render(user_data)
        result = open(outname, "rb").read()

        expected = u"".join(
            u"{} {} {}\n".format(line.var0, line.var1, line.var2)
            for line in user_data["mylist"]
        ).encode("utf-8")

        self.assertEqual(result, expected)

    def test_ignore_undefined_variables_text_template(self):

        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_text_template"
        )

        user_data = {}

        outname = get_secure_filename()

        template = TextTemplate(template_name, outname)
        error = True
        try:
            template.render(user_data)
            print(
                "Error: template contains variables that must be " "replaced"
            )
        except TemplateError:
            error = False

        self.assertFalse(error)

        template = TextTemplate(
            template_name, outname, ignore_undefined_variables=True
        )
        error = False
        try:
            template.render(user_data)
        except Exception:
            traceback.print_exc()
            error = True

        self.assertFalse(error)

    def test_remove_soft_page_breaks(self):
        template_xml = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_soft_page_break.odt"
        )
        outname = get_secure_filename()

        template = Template(template_xml, outname)
        soft_breaks = get_soft_breaks(
            template.content_trees[0], template.namespaces
        )
        self.assertEqual(len(soft_breaks), 2)

        template.remove_soft_breaks()
        soft_breaks = get_soft_breaks(
            template.content_trees[0], template.namespaces
        )
        self.assertEqual(len(soft_breaks), 0)

        template = Template(template_xml, outname)
        soft_breaks = get_soft_breaks(
            template.content_trees[0], template.namespaces
        )
        self.assertEqual(len(soft_breaks), 2)

        template.render(data={"list1": [1, 2, 3]})
        soft_breaks = get_soft_breaks(
            template.content_trees[0], template.namespaces
        )
        self.assertEqual(len(soft_breaks), 0)

        outodt = zipfile.ZipFile(outname, "r")
        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        nmspc = template.namespaces
        paragraphs = content_list.findall("//text:p", nmspc)
        bottom_break_paragraphs, middle_break_paragraphs = 0, 0
        for p in paragraphs:
            if not p.text:
                continue
            text = p.text.strip()
            if text == (
                u"This is a text with a margin at the bottom and a "
                u"soft-page-break"
            ):
                bottom_break_paragraphs += 1
            elif text == (
                u"This is a paragraph that is cut in half by a "
                u"soft-page-break. This text should not remain cut "
                u"in half after rendering."
            ):
                middle_break_paragraphs += 1
            else:
                self.fail(u"Unidentified text in result: {}".format(text))

        self.assertEqual(bottom_break_paragraphs, 3)
        self.assertEqual(middle_break_paragraphs, 3)

    def test_remove_soft_breaks_without_tail(self):
        template_xml = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_page_break_without_tail.odt"
        )
        t = Template(template_xml, get_secure_filename())
        soft_breaks = get_soft_breaks(t.content_trees[0], t.namespaces)
        assert len(soft_breaks) > 0

        t.remove_soft_breaks()
        soft_breaks = get_soft_breaks(t.content_trees[0], t.namespaces)
        assert len(soft_breaks) == 0

        t = Template(template_xml, get_secure_filename())
        soft_breaks = get_soft_breaks(t.content_trees[0], t.namespaces)
        assert len(soft_breaks) > 0

        t.render(
            data={
                "items": [
                    {"Amount": 3, "Currency": "D"},
                    {"Amount": 2, "Currency": "E"},
                    {"Amount": 1, "Currency": "C"},
                ]
            }
        )
        soft_breaks = get_soft_breaks(t.content_trees[0], t.namespaces)
        assert len(soft_breaks) == 0

    def test_invalid_links(self):
        u"""Check that exceptions are raised on link url and text mismatch"""

        templates = [
            ("py3o_invalid_link.odt", "url and text do not match.*"),
            ("py3o_invalid_link_old.odt", "url and text do not match.*"),
            ("py3o_invalid_link_none.odt", "Text not found for link.*"),
        ]

        for template, error in templates:
            template_fname = pkg_resources.resource_filename(
                "py3o.template", "tests/templates/{}".format(template)
            )
            t = Template(template_fname, get_secure_filename())
            with self.assertRaisesRegexp(TemplateException, error):
                t.render({"amount": 0.0})

    def test_table_cell_function_call(self):
        u"""Test function calls inside ODT table cells"""
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_table_cell_function_call.odt",
        )
        outname = get_secure_filename()
        template = Template(template_name, outname)

        data_dict = {
            "items": [
                Mock(val1=i, val2=range(i), val3=i ** 2) for i in range(1, 4)
            ],
            "document": Mock(total=6),
        }

        template.render(data_dict)

    def test_table_cell_for_loop(self):
        u"""Test for loop inside ODT table cells"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_table_cell_for_loop.odt"
        )
        outname = get_secure_filename()
        template = Template(template_name, outname)

        data_dict = {
            "items": [
                Mock(val1=i, val2=range(i), val3=i ** 2) for i in range(1, 4)
            ],
            "document": Mock(total=6),
        }

        template.render(data_dict)

    def test_odt_value_styles(self):
        u"""Test odf_value attribute and ODT styles"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_odt_value_styles.odt"
        )
        outname = get_secure_filename()
        template = Template(template_name, outname)

        data_dict = {
            "string_date": "1999-12-30",
            "odt_value_date": Mock(
                __str__=lambda s: "2009-07-06",
                odf_value=40000,
                odf_type="date",
            ),
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")
        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        expected_xml = lxml.etree.parse(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/odt_value_styles_result.xml"
            )
        )
        result = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )
        expected = lxml.etree.tostring(expected_xml, pretty_print=True).decode(
            "utf-8"
        )
        result = result.replace("\n", "").replace(" ", "")
        expected = expected.replace("\n", "").replace(" ", "")

        self.assertEqual(result, expected)

    def test_ods_value_styles(self):
        u"""Test odf_value attribute and ODS styles"""
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_ods_value_styles.ods"
        )
        outname = get_secure_filename()
        template = Template(template_name, outname)

        data_dict = {
            "string_date": "1999-12-30",
            "odf_value_date": Mock(
                __str__=lambda s: "2009-07-06",
                odf_value=40000,
                odf_type="date",
            ),
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")
        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        expected_xml = lxml.etree.parse(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/ods_value_styles_result.xml"
            )
        )
        result = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )
        expected = lxml.etree.tostring(expected_xml, pretty_print=True).decode(
            "utf-8"
        )
        result = result.replace("\n", "").replace(" ", "")
        expected = expected.replace("\n", "").replace(" ", "")

        self.assertEqual(result, expected)

    def test_input_fields_with_function(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_input_fields_for_function.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"datestring": "2017-10-02"}

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/input_fields_function_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_input_fields_with_control(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_for_loop_input_field.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"items": ["one", "two", "three"]}

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/input_fields_for_loop_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_variable_type_checking(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_ods_variable_type.ods"
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {
            "items": [
                Mock(val1=10, val2="toto"),
                Mock(val1=50.12, val2="titi"),
            ]
        }

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/py3o_ods_variable_type_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_template_with_function_call_multiline(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_template_function_call_multiline.odt",
        )

        outname = get_secure_filename()

        template = Template(template_name, outname)

        data_dict = {"multilinestring": "this\nis\na\nmulti\nline\nstring"}

        template.render(data_dict)
        outodt = zipfile.ZipFile(outname, "r")

        content_list = lxml.etree.parse(
            BytesIO(outodt.read(template.templated_files[0]))
        )

        result_a = lxml.etree.tostring(content_list, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template",
                "tests/templates/template_function_call_multiline_result.xml",
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e
