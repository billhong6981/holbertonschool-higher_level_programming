#!/usr/bin/python3
"""Unittest for Rectangle([..])"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """Test the Rectangle Class"""

    def setUp(self):
        """Initializes instance to zero"""
        Base.reset()

    def test_id_validation(self):
        "Normal test"""
        A = Square(3, 2)
        self.assertEqual(A.id, 1)
        self.assertEqual(A.size, 3)
        self.assertEqual(A.x, 2)

    def test_mul_id(self):
        """check multi id"""
        B1 = Square(20, 30)
        self.assertEqual(B1.id, 1)
        B2 = Square(10, 20)
        self.assertEqual(B2.id, 2)
        B3 = Square(10, 1, 1, 20)
        self.assertEqual(B3.id, 20)

    def test_args_optional(self):
        """check argumnents"""
        B0 = Square(3, 2)
        self.assertEqual([B0.x, B0.y], [2, 0])
        B0 = Square(4, 3, 5)
        self.assertEqual([B0.width, B0.x, B0.y, B0.id], [4, 3, 5, 2])

    def test_args_setter(self):
        """check args setter"""
        A = Square(3)
        A.width = 1
        self.assertEqual(A.width, 1)
        A.width = 5
        self.assertEqual(A.width, 5)
        A.x = 10
        self.assertEqual(A.x, 10)
        A.y = 20
        self.assertEqual(A.y, 20)

    def test_args_exception(self):
        """check args exceptions"""
        with self.assertRaises(TypeError):
            A = Square()

    def test_args_6_exception(self):
        """check args exceptions"""
        with self.assertRaises(TypeError):
            A = Square(8, 9, 10, 11, 12, 13)

    def test_str_width(self):
        """Check width is str"""
        with self.assertRaises(TypeError):
            Square("Hello", 3)

    def test_str_height(self):
        """Check height is str"""
        with self.assertRaises(TypeError):
            Square("Hello")

    def test_str_x(self):
        """Check x is str"""
        with self.assertRaises(TypeError):
            Square(3, "Hello")

    def test_str_y(self):
        """Check y is str"""
        with self.assertRaises(TypeError):
            Square(3, 10, "Hello")

    def test_list_width(self):
        """Check width is list"""
        with self.assertRaises(TypeError):
            Square([3], 2)

    def test_list_height(self):
        """Check height is list"""
        with self.assertRaises(TypeError):
            Square([2])

    def test_list_x(self):
        """Check x is list"""
        with self.assertRaises(TypeError):
            Square(3, [4])

    def test_list_y(self):
        """Check y is list"""
        with self.assertRaises(TypeError):
            Square(3, 2, [5])

    def test_area(self):
        """Simple area test"""
        A = Square(3)
        self.assertEqual(A.area(), 9)

    def test_inheritence(self):
        """Tests if Square is subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_args_1(self):
        """Test size of square"""
        A = Square(4)
        self.assertEqual([A.width, A.height], [4, 4])

    def test_attr_1(self):
        """Test attr of Rectangle, size should not created"""
        s1 = Square(2)
        with self.assertRaises(AttributeError):
            print(s1._Square__size)

if __name__ == '__main__':
    unittest.main()
