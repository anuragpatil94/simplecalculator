import unittest
import lib


class TestWithTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(lib.add_numbers(4, 2), 6, "Should be 6")

    def test_substract_two_numbers(self):
        self.assertEqual(lib.subtract_numbers(4, 2), 2, "Should be 2")

    def test_multiply_two_numbers(self):
        self.assertEqual(lib.multiply_numbers(4, 2), 8, "Should be 8")

    def test_divide_two_numbers(self):
        self.assertEqual(lib.divide_numbers(4, 2), 2, "Should be 2")

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, lib.divide_numbers, 4, 0)
