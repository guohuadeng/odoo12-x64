# -*- coding: utf-8 -*-

DEFAULT_MIMETYPE = "application/octet-stream"

FORMAT_WORD97 = "doc"
FORMAT_WORD2003 = "docx"
FORMAT_PDF = "pdf"
FORMAT_DOCBOOK = "docbook"
FORMAT_HTML = "html"
FORMAT_ODT = "odt"
FORMAT_ODS = "ods"
FORMAT_XLS = "xls"


class UnkownFormatException(Exception):
    pass


class Format(object):

    def __init__(self, name, odfname, mimetype=DEFAULT_MIMETYPE, native=False):
        self.name = name
        self.odfname = odfname
        self.mimetype = mimetype
        self.native = native


class Formats(object):

    def __init__(self):

        self._formats = {
            FORMAT_WORD97: Format(
                FORMAT_WORD97, "MS Word 97", "application/msword"
            ),
            FORMAT_WORD2003: Format(
                FORMAT_WORD2003, "MS Word 2003 XML",
                "application/vnd.openxmlformats-officedocument"
                ".wordprocessingml.document"
            ),
            FORMAT_PDF: Format(
                FORMAT_PDF, "writer_pdf_Export", "application/pdf"
            ),
            FORMAT_DOCBOOK: Format(
                FORMAT_DOCBOOK, "DocBook File", "application/xml"
            ),
            FORMAT_HTML: Format(FORMAT_HTML, "HTML", "text/html"),
            FORMAT_ODT: Format(
                FORMAT_ODT, "writer8",
                "application/vnd.oasis.opendocument.text",
                native=True,
            ),
            FORMAT_ODS: Format(
                FORMAT_ODS, "calc8",
                "application/vnd.oasis.opendocument.spreadsheet",
                native=True,
            ),
            FORMAT_XLS: Format(
                FORMAT_XLS, "MS Excel 97", "application/msexcel"
            ),
        }

    def get_format(self, name):
        f = self._formats.get(name)

        if not f:
            raise UnkownFormatException("Format {} is unkown".format(name))

        return f

    def get_known_format_names(self, nativeonly=False):
        """return the a list of names that can be used as format names in
        py3o.template.

        :param nativeonly: a boolean flag. If set to True will only return
        native formats.
        :type nativeonly: bool

        :return: list of chars
        :returntype: list

        :raises: nothing
        """
        if nativeonly:
            return [
                f for f in self._formats if self.get_format(f).native
            ]
        else:
            return [f for f in self._formats]
