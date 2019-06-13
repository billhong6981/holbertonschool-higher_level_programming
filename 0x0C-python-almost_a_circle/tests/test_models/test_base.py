#!/usr/bin/python3
"""Unittest for Base([..])"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test the Base Class"""

    def test_id_validation(self):
        "Normal test"""
        A = Base()
        self.assertEqual(A.id, 1)

    def test_mul_id(self):
        """check multi id"""
        B1 = Base()
        self.assertEqual(B1.id, 2)
        B2 = Base()
        self.assertEqual(B2.id, 3)
        B3 = Base(10)
        self.assertEqual(B3.id, 10)
        B4 = Base(10)
        self.assertEqual(B4.id, 10)
        B5 = Base()
        self.assertEqual(B5.id, 4)

    def test_id_tuple(self):
        """check id is tuple"""
        B0 = Base((3, 2))
        self.assertEqual(B0.id, (3, 2))

    def test_id_str(self):
        """check id is string"""
        B6 = Base("Hello")
        self.assertEqual(B6.id, "Hello")

    def test_id_list(self):
        """check id is list"""
        B7 = Base([3, 2])
        self.assertEqual(B7.id, [3, 2])

    def test_id_dict(self):
        """check id is dictionary"""
        B7 = Base({"key": 2})
        self.assertEqual(B7.id, {"key": 2})

    def test_id_set(self):
        """check id is set"""
        B7 = Base({3, 2})
        self.assertEqual(B7.id, {3, 2})

    def test_id_float(self):
        """check id is float"""
        B7 = Base(2.17)
        self.assertEqual(B7.id, 2.17)

    def test_id_isprivate(self):
        """check id is private attribute"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
