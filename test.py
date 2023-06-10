import unittest
from divide import divide_numbers

class TestDivideNumbers(unittest.TestCase):
    def test_negative_numbers(self):
        """Test dividing a negative dividend by a positive divisor."""
        result = divide_numbers(-10, 2)
        self.assertEqual(result, -5)
        
        """Test dividing a positive dividend by a negative divisor."""
        result = divide_numbers(10, -2)
        self.assertEqual(result, -5)
        
        """Test dividing two negative numbers."""
        result = divide_numbers(-10, -2)
        self.assertEqual(result, 5)
        
    def test_positive_numbers(self):
        """Test dividing two positive numbers."""
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)
