#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, -3, 20, 15]), 20)

    def test_all_same_values(self):
        """Test with all same values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.1]), 3.9)

    def test_large_list(self):
        """Test with a large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_no_argument(self):
        """Test with no argument passed"""
        self.assertIsNone(max_integer())

    def test_single_negative(self):
        """Test with a single negative number"""
        self.assertEqual(max_integer([-5]), -5)

    def test_zero_in_list(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([0, -1, -5, -10]), 0)

    def test_positive_and_zero(self):
        """Test with positive numbers and zero"""
        self.assertEqual(max_integer([0, 5, 10, 3]), 10)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([10, 5]), 10)

    def test_duplicates_max(self):
        """Test with duplicate max values"""
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)


if __name__ == '__main__':
    unittest.main()
