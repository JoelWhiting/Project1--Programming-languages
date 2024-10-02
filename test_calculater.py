import unittest
from roman_calc import roman_to_int, int_to_roman, calculate

class TestRomanCalculator(unittest.TestCase):
    
    # Tests for roman_to_int function
    def test_roman_to_int_valid(self):
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XLII"), 42)
        self.assertEqual(roman_to_int("MMXXIV"), 2024)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    def test_roman_to_int_invalid(self):
        self.assertRaises(ValueError, roman_to_int, "IIII")  # Invalid Roman numeral
        self.assertRaises(ValueError, roman_to_int, "ABC")   # Invalid characters
        self.assertRaises(ValueError, roman_to_int, "")      # Empty string

    # Tests for int_to_roman function
    def test_int_to_roman_valid(self):
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(42), "XLII")
        self.assertEqual(int_to_roman(2024), "MMXXIV")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")

    def test_int_to_roman_edge_cases(self):
        # Edge cases will be handled in the `calculate` function, not directly in `int_to_roman`
        self.assertEqual(calculate("0"), "0 does not exist in Roman numerals.")
        self.assertEqual(calculate("-5"), "Negative numbers can’t be represented in Roman numerals.")
        self.assertEqual(calculate("4000"), "You’re going to need a bigger calculator.")

    # Tests for calculate function
    def test_calculate_valid(self):
        self.assertEqual(calculate("X + IX"), "XIX")
        self.assertEqual(calculate("L - X"), "XL")
        self.assertEqual(calculate("XLII * II"), "LXXXIV")
        self.assertEqual(calculate("MM / II"), "M")
        self.assertEqual(calculate("(X + IX) * II"), "XXXVIII")

    def test_calculate_invalid(self):
        self.assertEqual(calculate("IIII + X"), "I don’t know how to read this.")
        self.assertEqual(calculate("X + ABC"), "I don’t know how to read this.")
        self.assertEqual(calculate("X / 0"), "I don’t know how to read this.")
        self.assertEqual(calculate("X - L"), "Negative numbers can’t be represented in Roman numerals.")
        self.assertEqual(calculate("I / II"), "There is no concept of a fractional number in Roman numerals.")
        self.assertEqual(calculate("MMM + M"), "You’re going to need a bigger calculator.")

if __name__ == '__main__':
    unittest.main()
