#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
      A = [1, 2, 3, 4]
      self.assertEqual(max_integer(A), 4)

    def test_float(self):
      B = [3, 4, 6, 7.1]
      self.assertEqual(max_integer(B), 7.1)

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
