#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test Max Integer Class"""

    def test_max_integer(self):
        "Normal test"""
        A = [1, 2, 3, 4]
        self.assertEqual(max_integer(A), 4)

    def test_at_begin(self):
        """max at biginning"""
        B = [8, 4, 6]
        self.assertEqual(max_integer(B), 8)

    def test_at_middle(self):
        """max at middle"""
        self.assertEqual(max_integer([2, 5, 3]), 5)

    def test_at_end(self):
        """max at the end"""
        self.assertEqual(max_integer([3, 5, 7]), 7)

    def test_one_negative(self):
        """Test for “one negative number in the list” exists"""
        self.assertEqual(max_integer([-3]), -3)

    def test_only_negative(self):
        """Test for only negative number in list"""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_empty(self):
        A = []
        self.assertEqual(max_integer(A), None)

    def test_one_element(self):
        A = [1]
        self.assertEqual(max_integer(A), 1)

    def test_string(self):
        A = [1, "hello", 3]
        with self.assertRaises(TypeError):
            max_integer(A)

if __name__ == '__main__':
    unittest.main()
