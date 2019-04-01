# -*- encoding: utf-8 -*-
from py3o.template.data_struct import Py3oDataError
from py3o.template.helpers import Py3oConvertor

import unittest
import os

import lxml.etree
import pkg_resources
import six

from pyjon.utils import get_secure_filename

from py3o.template.main import move_siblings, detect_keep_boundary, Template

from py3o.template.data_struct import Py3oName

if six.PY3:
    # noinspection PyUnresolvedReferences
    from unittest.mock import Mock
elif six.PY2:
    # noinspection PyUnresolvedReferences
    from mock import Mock


class TestHelpers(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        template_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_example_template.odt"
        )

        outname = get_secure_filename()

        self.reference_template = Template(template_name, outname)
        os.unlink(outname)

    def test_move_1(self):
        """test that siblings are properly moved without keeping boundaries"""
        template_one_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_one.xml"
        )
        test_template_one = lxml.etree.parse(template_one_name)
        start = test_template_one.find("mystruct/start")
        end = test_template_one.find("mystruct/end")
        new_ = lxml.etree.Element("finishcontainer")

        move_siblings(start, end, new_)

        result_s = lxml.etree.tostring(
            test_template_one, pretty_print=True
        ).decode("utf-8")

        expected_result = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_one_result.xml"
            )
        ).read()

        expected_result = (
            expected_result.replace("\n", "").replace(" ", "").strip()
        )

        result_s = result_s.replace("\n", "").replace(" ", "").strip()

        assert result_s == expected_result

    def test_move_2(self):
        """start.tail is correctly copied without keeping boundaries"""
        template_two_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_two.xml"
        )
        test_template_two = lxml.etree.parse(template_two_name)
        start = test_template_two.find("mystruct/start")
        end = test_template_two.find("mystruct/end")
        new_ = lxml.etree.Element("finishcontainer")

        move_siblings(start, end, new_)

        result_s = lxml.etree.tostring(
            test_template_two, pretty_print=True
        ).decode("utf-8")

        expected_result = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_two_result.xml"
            )
        ).read()

        expected_result = (
            expected_result.replace("\n", "").replace(" ", "").strip()
        )

        result_s = result_s.replace("\n", "").replace(" ", "").strip()

        assert result_s == expected_result

    def test_move_keep_boundaries(self):
        """test that siblings are properly moved keeping boundaries"""
        template_three_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_three.xml"
        )
        test_template_three = lxml.etree.parse(template_three_name)
        start = test_template_three.find("mystruct/start")
        end = test_template_three.find("mystruct/end")

        new_ = lxml.etree.Element("finishcontainer")

        move_siblings(
            start, end, new_, keep_start_boundary=True, keep_end_boundary=True
        )

        result_s = lxml.etree.tostring(
            test_template_three, pretty_print=True
        ).decode("utf-8")

        expected_result = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_three_result.xml"
            )
        ).read()

        expected_result = (
            expected_result.replace("\n", "").replace(" ", "").strip()
        )

        result_s = result_s.replace("\n", "").replace(" ", "").strip()

        assert result_s == expected_result

    def test_move_2_keep_boundaries(self):
        """test that start.tail is correctly copied keeping boundaries"""
        template_four_name = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_four.xml"
        )
        test_template_four = lxml.etree.parse(template_four_name)
        start = test_template_four.find("mystruct/start")
        end = test_template_four.find("mystruct/end")

        new_ = lxml.etree.Element("finishcontainer")

        move_siblings(
            start, end, new_, keep_start_boundary=True, keep_end_boundary=True
        )

        result_s = lxml.etree.tostring(
            test_template_four, pretty_print=True
        ).decode("utf-8")

        expected_result = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_four_result.xml"
            )
        ).read()

        expected_result = (
            expected_result.replace("\n", "").replace(" ", "").strip()
        )

        result_s = result_s.replace("\n", "").replace(" ", "").strip()

        assert result_s == expected_result

    def test_get_user_variables(self):
        source_odt_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_example_template.odt"
        )
        outfilename = get_secure_filename()

        template = Template(source_odt_filename, outfilename)

        user_vars = template.get_user_variables()

        expected_vars = [
            "line.val1",
            "line.val2",
            "line.val3",
            "item.Amount",
            "item.Currency",
            "item.InvoiceRef",
            "document.total",
        ]
        assert set(user_vars) == set(expected_vars)

    def test_convertor(self):
        source_odt_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_if_parser.odt"
        )
        outfilename = get_secure_filename()

        template = Template(source_odt_filename, outfilename)

        user_vars = template.get_user_variables()
        expressions = template.get_all_user_python_expression()
        py_expression = template.convert_py3o_to_python_ast(expressions)
        convertor = Py3oConvertor()
        data_struct = convertor(py_expression)

        assert "objects" in data_struct
        objs = data_struct["objects"]
        assert "company_label" in objs
        assert "name" in objs
        assert isinstance(objs["company_label"], Py3oName)
        assert isinstance(objs["name"], Py3oName)
        #         assert data_struct == Py3oModule(
        #             {
        #                 'objects': Py3oArray(
        #                             {
        #                                 'company_label': Py3oName({}),
        #                                 'name': Py3oName({})
        #                             }
        #                 )
        #             }
        #         )
        expected_vars = ["registration.name", "registration.company_label"]
        assert set(user_vars) == set(expected_vars)

    def test_get_user_instructions(self):
        source_odt_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_example_template.odt"
        )
        outfilename = get_secure_filename()

        template = Template(source_odt_filename, outfilename)

        user_instructions = template.get_user_instructions()

        expected_vars = [
            'for="line in items"',
            "/for",
            'for="item in items"',
            "if=\"item.InvoiceRef=='#1234'\"",
            "/if",
            "/for",
        ]
        assert set(user_instructions) == set(expected_vars)

    def test_calc(self):
        """Test date source extraction in ods files"""
        source_ods_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/py3o_simple_calc.ods"
        )
        outfilename = get_secure_filename()

        template = Template(source_ods_filename, outfilename)

        expressions = template.get_all_user_python_expression()
        expected_expressions = [
            'for="item in items"',
            "item.col1",
            "item.col2",
            "item.col3",
            "item.col4",
            "/for",
        ]
        self.assertEqual(expressions, expected_expressions)

        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        user_data = {
            "items": [
                Mock(col0="0", col1=1, col2=2.0, col3="?", col4="!"),
                Mock(col0=0, col1=1.0, col2="2", col3="?", col4="!"),
                Mock(col0=0.0, col1="1", col2=2, col3="?", col4="!"),
            ]
        }

        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "items": [
                    dict(col1=1, col2=2.0, col3="?", col4="!"),
                    dict(col1=1.0, col2="2", col3="?", col4="!"),
                    dict(col1="1", col2=2, col3="?", col4="!"),
                ]
            },
        )

    def test_detect_boundary_false(self):
        """boundary detection should say no!!"""

        source_xml_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/keepboundary_detection_false.xml"
        )

        test_xml = lxml.etree.parse(source_xml_filename)
        starts, ends = self.reference_template.find_instructions(
            [test_xml], self.reference_template.namespaces
        )
        for start, base in starts:
            end = ends[id(start)]
            keep_start, keep_end = detect_keep_boundary(
                start, end, self.reference_template.namespaces
            )
            assert keep_start is False
            assert keep_end is False

    def test_detect_boundary_true(self):
        """boundary detection should say yes!!"""

        source_xml_filename = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/keepboundary_detection_true.xml"
        )

        test_xml = lxml.etree.parse(source_xml_filename)
        starts, ends = self.reference_template.find_instructions(
            [test_xml], self.reference_template.namespaces
        )
        for index, (start, base) in enumerate(starts):
            end = ends[id(start)]
            keep_start, keep_end = detect_keep_boundary(
                start, end, self.reference_template.namespaces
            )
            if index == 0:
                assert keep_start is False
                assert keep_end is True

            else:
                assert False, "We should find one single link"

    def test_move_siblings_1(self):
        template_xml = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_siblings.xml"
        )
        test_xml = lxml.etree.parse(template_xml)
        starts, ends = self.reference_template.find_instructions(
            [test_xml], self.reference_template.namespaces
        )

        assert len(starts) == 1
        assert len(ends) == 1

        start, _ = starts[0]
        end = ends[id(start)]

        keep_start, keep_end = detect_keep_boundary(
            start, end, self.reference_template.namespaces
        )

        assert keep_start is True
        assert keep_end is False

        new_ = lxml.etree.Element("finishcontainer")

        start_parent = start.getparent()
        end_parent = end.getparent()

        start.getparent().remove(start)
        end.getparent().remove(end)

        move_siblings(
            start_parent,
            end_parent,
            new_,
            keep_start_boundary=keep_start,
            keep_end_boundary=keep_end,
        )

        result_a = lxml.etree.tostring(test_xml, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_siblings_result_1.xml"
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_move_siblings_2(self):
        template_xml = pkg_resources.resource_filename(
            "py3o.template", "tests/templates/move_siblings.xml"
        )
        test_xml = lxml.etree.parse(template_xml)
        starts, ends = self.reference_template.find_instructions(
            [test_xml], self.reference_template.namespaces
        )

        assert len(starts) == 1
        assert len(ends) == 1

        start, base = starts[0]
        end = ends[id(start)]

        keep_start, keep_end = detect_keep_boundary(
            start, end, self.reference_template.namespaces
        )

        assert keep_start is True
        assert keep_end is False

        self.reference_template.handle_link(start, base, end)
        result_a = lxml.etree.tostring(test_xml, pretty_print=True).decode(
            "utf-8"
        )

        result_e = open(
            pkg_resources.resource_filename(
                "py3o.template", "tests/templates/move_siblings_result_2.xml"
            )
        ).read()

        result_a = result_a.replace("\n", "").replace(" ", "")
        result_e = result_e.replace("\n", "").replace(" ", "")

        assert result_a == result_e

    def test_content_tree_with_child_instruction(self):
        template_xml = pkg_resources.resource_filename(
            "py3o.template",
            "tests/templates/py3o_example_invalid_template.odt",
        )
        t = Template(template_xml, get_secure_filename())
        usr_insts = t.get_user_instructions()
        assert usr_insts == [
            'for="item in items"',
            "/for",
            'for="item in items',
            "2",
            '"',
            "/for",
        ]

    def __load_and_convert_template(self, path):
        template_xml = pkg_resources.resource_filename("py3o.template", path)
        t = Template(template_xml, get_secure_filename())
        expressions = t.get_all_user_python_expression()
        py_expr = t.convert_py3o_to_python_ast(expressions)
        return py_expr

    def test_access_global_variable_inside_loop(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_global_variable_inside_loop.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"global_var": Mock(val=1), "my4list": [0, 1, 2, 3]}
        json_str = res.render(user_data)
        self.assertEquals(
            json_str, {"global_var": dict(val=1), "my4list": [0, 1, 2, 3]}
        )

    def test_access_in_loop_variable(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_in_loop_variable.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"my2list": [0, 1, 2, 3, 4]}
        json_str = res.render(user_data)
        assert json_str == {"my2list": [0, 1, 2, 3, 4]}

    def test_access_global_variable(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_global_variable.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"var0": 0, "var1": 1, "var2": 2}
        json_str = res.render(user_data)
        assert json_str == {"var0": 0, "var1": 1, "var2": 2}

    def test_iterable_with_global_attribute(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_iterable_with_global_attribute.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"foo": Mock(my2list=[0, 1, 2, 3, 4])}
        json_str = res.render(user_data)
        assert json_str == {"foo": {"my2list": [0, 1, 2, 3, 4]}}

    def test_two_for_list_on_same_attribute(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_two_for_list_on_same_attribute.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "foo": Mock(my2list=[0, 1, 2, 3, 4], my3list=[5, 6, 7, 8])
        }
        json_str = res.render(user_data)
        assert json_str == {
            "foo": {"my2list": [0, 1, 2, 3, 4], "my3list": [5, 6, 7, 8]}
        }

    def test_access_in_loop_variable_with_attribute(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_in_loop_variable_with_attribute.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"my3list": [Mock(val=0), Mock(val=1), Mock(val=2)]}
        json_str = res.render(user_data)
        assert json_str == {"my3list": [{"val": 0}, {"val": 1}, {"val": 2}]}

    def test_access_in_loop_variable_with_multiple_attribute(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/"
            "py3o_access_in_loop_variable_with_multiple_attribute.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "my3list": [
                Mock(foo=Mock(val=0)),
                Mock(foo=Mock(val=1)),
                Mock(foo=Mock(val=2)),
            ]
        }
        json_str = res.render(user_data)
        assert json_str == {
            "my3list": [
                {"foo": {"val": 0}},
                {"foo": {"val": 1}},
                {"foo": {"val": 2}},
            ]
        }

    def test_access_parent_variable_in_nested_loop(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_parent_variable_in_nested_loop.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"my9list": [Mock(val=10), Mock(val=11)]}
        json_str = res.render(user_data)
        assert json_str == {"my9list": [{"val": 10}, {"val": 11}]}

    def test_access_parent_variable_in_nested_loop_with_attribute(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/"
            "py3o_access_parent_variable_in_nested_loop_with_attribute.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "my10list": [
                Mock(my_list=[Mock(val=10), Mock(val=11)]),
                Mock(my_list=[Mock(val=20), Mock(val=21), Mock(val=22)]),
            ]
        }
        json_str = res.render(user_data)
        assert json_str == {
            "my10list": [
                {"my_list": [{"val": 10}, {"val": 11}]},
                {"my_list": [{"val": 20}, {"val": 21}, {"val": 22}]},
            ]
        }

    def test_access_variable_in_nested_loop(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/" "py3o_access_variable_in_nested_loop.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"my8list": [[10, 11, 12], [20, 21, 22, 23]]}
        json_str = res.render(user_data)
        assert json_str == {"my8list": [[10, 11, 12], [20, 21, 22, 23]]}

    def test_bad_user_data(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_access_global_variable_inside_loop.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {}
        with self.assertRaises(Py3oDataError):
            res.render(user_data)

    def test_test_statement(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_test_statement.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"var0": 42, "myvar": Mock(var0=43, var1="val")}
        json_dict = res.render(user_data)
        assert json_dict == {"var0": 42, "myvar": {"var0": 43, "var1": "val"}}

    def test_double_loop_on_same_object(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_double_loop_on_same_object.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "varlist": [Mock(var0=42, var1=-42), Mock(var0=170, var1=-170)]
        }
        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "varlist": [
                    {"var0": 42, "var1": -42},
                    {"var0": 170, "var1": -170},
                ]
            },
        )

    def test_false_value(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/test_false_value.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        false_mock = Mock()
        false_mock.__nonzero__ = lambda x: False
        false_mock.__bool__ = lambda x: False

        user_data = {"false_value": false_mock}
        json_dict = res.render(user_data)
        assert json_dict == {"false_value": u""}

    def test_enumerate(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_enumerate.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {"mylist": [10, 9, 8, 7, 6]}
        json_dict = res.render(user_data)
        assert json_dict == {"mylist": [10, 9, 8, 7, 6]}

    def test_enumerate_attribute_access(self):
        """For loop on enumerate: only attributes used in body are extracted.
        Since mylist is given as an argument to enumerate, a known builtin
        function, Py3oConvertor should be able to recognize that val refers
        to the elements of mylist.
        """
        expressions = [
            'for="i, val in enumerate(mylist)"',
            "i",
            "val.var0",
            "val.var2",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "mylist": [
                Mock(var0="0", var1=1, var2=2.0),
                Mock(var0=0, var1=1.0, var2="2"),
                Mock(var0=0.0, var1="1", var2=2),
            ]
        }
        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "mylist": [
                    dict(var0="0", var2=2.0),
                    dict(var0=0, var2="2"),
                    dict(var0=0.0, var2=2),
                ]
            },
        )

    def test_unknown_iterable_call(self):
        """For loop on unknown function call: extract the entire object"""

        expressions = [
            'for="i, val in not_enumerate(mylist)"',
            "i",
            "val.var0",
            "val.var2",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "mylist": [
                Mock(var0="0", var1=1, var2=2.0),
                Mock(var0=0, var1=1.0, var2="2"),
                Mock(var0=0.0, var1="1", var2=2),
            ]
        }
        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "mylist": [
                    user_data["mylist"][0],
                    user_data["mylist"][1],
                    user_data["mylist"][2],
                ]
            },
        )

    def test_template_function_call(self):
        py_expr = self.__load_and_convert_template(
            "tests/templates/py3o_template_function_call.odt"
        )
        p = Py3oConvertor()
        res = p(py_expr)
        user_data = {"amount": 32.123}
        json_dict = res.render(user_data)
        assert json_dict == {"amount": 32.123}

    def test_template_function_call_in_for_loop(self):
        expressions = [
            'for="item in object.list"',
            "item.test",
            "format_number(item.var)",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        user_data = {
            "object": Mock(
                list=[Mock(var=32.123, test="2.3"), Mock(var=43.2, test="1.0")]
            )
        }
        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "object": {
                    "list": [
                        {"var": 32.123, "test": "2.3"},
                        {"var": 43.2, "test": "1.0"},
                    ]
                }
            },
        )

    def test_double_for_loop_on_same_attribute(self):
        expressions = [
            'for="item in root.object.list"',
            "item.var1",
            "/for",
            'for="item in root.object.list"',
            "item.var0",
            "/for",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)

        user_data = {
            "root": Mock(
                object=Mock(
                    list=[Mock(var0=42, var1=-42), Mock(var0=170, var1=-170)]
                )
            )
        }
        json_dict = res.render(user_data)
        self.assertEqual(
            json_dict,
            {
                "root": {
                    "object": {
                        "list": [
                            dict(var0=42, var1=-42),
                            dict(var0=170, var1=-170),
                        ]
                    }
                }
            },
        )

    def test_if(self):
        expressions = ['if="item.mytest"', "item.myvar", "item.myvar2", "/if"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"item": Mock(mytest=0, myvar=1, myvar2=2)})

        assert json_dict == {"item": {"mytest": 0, "myvar": 1, "myvar2": 2}}

    def test_if_global(self):
        expressions = ['if="mytest"', "item.myvar", "item.myvar2", "/if"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"item": Mock(myvar=1, myvar2=2), "mytest": 0})

        assert json_dict == {"mytest": 0, "item": {"myvar": 1, "myvar2": 2}}

    def test_if_global_array(self):
        expressions = [
            'for="var in myarray"',
            'if="var"',
            "var",
            "/if",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"myarray": list(range(0, 5))})

        assert json_dict == {"myarray": list(range(0, 5))}

    def test_if_in_for(self):
        expressions = [
            'for="item in object.mylist"',
            'if="item.mytest"',
            "item.myvar",
            "item.myvar2",
            "/if",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render(
            {
                "object": Mock(
                    mylist=[
                        Mock(mytest=0, myvar=1, myvar2=2),
                        Mock(mytest=3, myvar=4, myvar2=5),
                        Mock(mytest=6, myvar=7, myvar2=8),
                    ]
                )
            }
        )

        assert json_dict == {
            "object": {
                "mylist": [
                    {"mytest": 0, "myvar": 1, "myvar2": 2},
                    {"mytest": 3, "myvar": 4, "myvar2": 5},
                    {"mytest": 6, "myvar": 7, "myvar2": 8},
                ]
            }
        }

    def test_if_comparator(self):
        expressions = ['if="a in b"', "/if"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"a": 1, "b": [0, 1, 2]})

        assert json_dict == {"a": 1, "b": [0, 1, 2]}

    def test_if_comparator_literal(self):
        expressions = ['if="a == 1"', "/if"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"a": 1})

        self.assertEqual(json_dict, {"a": 1})

    # Test function

    def test_function_in_for(self):
        expressions = [
            'for="item in object.mylist"',
            "format_date(item.date)",
            "/for",
        ]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render(
            {
                "object": Mock(
                    mylist=[
                        Mock(date="2015-12-13"),
                        Mock(date="2015-12-14"),
                        Mock(date="2015-12-15"),
                    ]
                )
            }
        )

        assert json_dict == {
            "object": {
                "mylist": [
                    {"date": "2015-12-13"},
                    {"date": "2015-12-14"},
                    {"date": "2015-12-15"},
                ]
            }
        }

    def test_function_keywords(self):
        expressions = ["myfunc(object.var, k=object.k)"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"object": Mock(var=0, k=1)})

        assert json_dict == {"object": {"var": 0, "k": 1}}

    def test_function_array(self):
        expressions = ['for="var in myarray"', "myfunc(var)", "/for"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        json_dict = res.render({"myarray": [0, 1, 2, 3]})

        assert json_dict == {"myarray": [0, 1, 2, 3]}

    def test_empty_for_loop(self):
        u"""Test ast extraction on for loops whose body do not use any data"""
        expressions = ['for="var in myarray"', "/for"]
        py_expr = Template.convert_py3o_to_python_ast(expressions)
        self.assertEqual(py_expr.strip(), "for var in myarray:\n pass")
        p = Py3oConvertor()
        res = p(py_expr)
        data = {"myarray": [0, 1, 2, 3]}
        json_dict = res.render(data)
        self.assertEqual(json_dict, data)

    def test_unpack_from_data_source(self):

        expressions = ['for="a, b in myarray"', "a", "b.c", "/for"]

        py_expr = Template.convert_py3o_to_python_ast(expressions)
        p = Py3oConvertor()
        res = p(py_expr)
        data = {"myarray": [(1, Mock(c=2, d=3)), (4, Mock(c=5, d=6))]}
        json_dict = res.render(data)
        self.assertEqual(
            json_dict, {"myarray": [[1, {"c": 2}], [4, {"c": 5}]]}
        )
