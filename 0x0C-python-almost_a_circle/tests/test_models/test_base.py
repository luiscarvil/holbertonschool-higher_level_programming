#!/usr/bin/python3
"""
Unittest classes
"""
import unittest
import pycodestyle
from models.base import Base, __doc__
from models.rectangle import Rectangle
from models.square import Square


class Base_test_class(unittest.TestCase):
    """
    Unittest for testing instantiation
    """
    def test_base(self):
        b = Base(1)
        self.assertEqual(b.id, 1)
        b.id = 9
        self.assertEqual(b.id, 9)

    def test_without_arg(self):
        self.assertEqual(Base().id, (Base().id) - 1)

    def test_more_arg(self):
        b1, b2, b3 = Base(), Base(), Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_nb_instance(self):
        b1, b2, b3 = Base(), Base(1), Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id(self):
        self.assertEqual(5, Base(5).id)
        b, b.id = Base(10), 5
        self.assertEqual(5, b.id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_base_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_num_id(self):
        self.assertEqual(range(9), Base(range(9)).id)

    def test_base_dict(self):
        self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_base_NaN_id(self):
        self.assertNotEqual(float('NaN'), Base(float('NaN')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_list_id(self):
        self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)

    def test_docstring(self):
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__.strip()) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.create.__doc__.strip()) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__.strip()) > 0)

    def test_conformance(self):
        fchecker = pycodestyle.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()
        print("Found %s errors (and warnings)" % file_errors)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""
    def test_to_json_string_noArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_moreArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_rectangle_type(self):
        self.assertEqual(str, type(Base.to_json_string(
            [Rectangle(1, 2, 3, 4, 5).to_dictionary()])))

    def test_to_json_string_rectangle_aDict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_twoDicts(self):
        list_dicts = [Rectangle(2, 3, 5, 19, 2).to_dictionary(), Rectangle(
            4, 2, 4, 1, 12).to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_Type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_Dict(self):
        self.assertTrue(len(
            Base.to_json_string([Square(10, 2, 3, 4).to_dictionary()])) == 39)

    def test_to_json_string_square_Dicts(self):
        list_dicts = [Square(2, 10, 4, 3).to_dictionary(), Square(
            4, 5, 2, 21).to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empList(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))
