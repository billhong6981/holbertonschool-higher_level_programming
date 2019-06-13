#!/usr/bin/python3
"""Unittest for Rectangle([..])"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test the Rectangle Class"""

    def setUp(self):
        """Initializes instance to zero"""
        Base.reset()

    def test_id_validation(self):
        "Normal test"""
        A = Rectangle(3, 2)
        self.assertEqual(A.id, 1)
        self.assertEqual(A.width, 3)
        self.assertEqual(A.height, 2)

    def test_mul_id(self):
        """check multi id"""
        B1 = Rectangle(20, 30)
        self.assertEqual(B1.id, 1)
        B2 = Rectangle(10, 20)
        self.assertEqual(B2.id, 2)
        B3 = Rectangle(10, 2, 1, 1, 20)
        self.assertEqual(B3.id, 20)

    def test_args_optional(self):
        """check argumnents"""
        B0 = Rectangle(3, 2)
        self.assertEqual([B0.x, B0.y], [0, 0])
        B0 = Rectangle(4, 3, 5)
        self.assertEqual([B0.width, B0.height, B0.x, B0.y, B0.id], [
            4, 3, 5, 0, 2])

    def test_args_setter(self):
        """check args setter"""
        A = Rectangle(3, 2)
        A.width = 1
        self.assertEqual(A.width, 1)
        A.height = 5
        self.assertEqual(A.height, 5)
        A.x = 10
        self.assertEqual(A.x, 10)
        A.y = 20
        self.assertEqual(A.y, 20)

    def test_args_exception(self):
        """check args exceptions"""
        with self.assertRaises(TypeError):
            A = Rectangle()

    def test_args_1_exception(self):
        """check args exceptions"""
        with self.assertRaises(TypeError):
            A = Rectangle(2)

    def test_args_6_exception(self):
        """check args exceptions"""
        with self.assertRaises(TypeError):
            A = Rectangle(8, 9, 10, 11, 12, 13)

    def test_str_width(self):
        """Check width is str"""
        with self.assertRaises(TypeError):
            Rectangle("Hello", 3)

    def test_str_height(self):
        """Check height is str"""
        with self.assertRaises(TypeError):
            Rectangle(3, "Hello")

    def test_str_x(self):
        """Check x is str"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, "Hello")

    def test_str_y(self):
        """Check y is str"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 10, "Hello")

    def test_list_width(self):
        """Check width is list"""
        with self.assertRaises(TypeError):
            Rectangle([3], 2)

    def test_list_height(self):
        """Check height is list"""
        with self.assertRaises(TypeError):
            Rectangle(3, [2])

    def test_list_x(self):
        """Check x is list"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, [4])

    def test_list_y(self):
        """Check y is list"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 4, [5])

    def test_area(self):
        """Simple area test"""
        A = Rectangle(3, 2)
        self.assertEqual(A.area(), 6)

    def test_inheritence(self):
        """Tests if Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

if __name__ == '__main__':
    unittest.main()
