#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        """ check values in max_integer """
        self.assertEqual(max_integer([1, 7, 3]), 7)
        self.assertEqual(max_integer([-7, 5, 3]), 5)
        self.assertEqual(max_integer([-2, -3, -7]), -2)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1, 3] * 2), 3)
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_tuple(self):
        """ diferent than list """
        with self.assertRaises(TypeError):
            tmp = max_integer((2, 1), (2, 3))

    def test_empty(self):
        """ list with empty values """
        self.assertEqual(max_integer([]), None)

    def test_docstringmod(self):
        """Check docstring for module"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(m is not None and len(m) > 0)

    def test_docstringfunc(self):
        f = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(f is not None and len(f) > 5)

if __name__ == '__main__':
    unittest.main()
