""" Homework 8 task 1 """


import unittest


class StringProcessor:
    """Class StringProcessor"""
    def reverse_string(self, s: str) -> str:
        """Returns a reversed string"""
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Makes the first letter of a string uppercase."""
        if not s:
            return s
        return s[0].upper() + s[1:]

    def count_vowels(self, s: str) -> int:
        """Returns the number of vowels in a string"""
        vowels = "АЕЄИІЇОУЮЯаеєиіїоуюя"
        return sum(1 for char in s if char in vowels)


class TestStringProcessor(unittest.TestCase):
    """Class TEST"""
    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_string_normal(self):
        """Test reverse string usual"""
        self.assertEqual(self.processor.reverse_string("hello"), "olleh")

    def test_reverse_string_with_symbols(self):
        """Test reverse string with symbols"""
        self.assertEqual(self.processor.reverse_string("abc123!"), "!321cba")

    @unittest.skip("Відома проблема з обробкою порожнього рядка")
    def test_reverse_string_empty(self):
        """Test reverse string with empty string"""
        self.assertEqual(self.processor.reverse_string(""), "")

    def test_capitalize_string_normal(self):
        """Test capitalize string usual"""
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")

    def test_capitalize_string_already_capitalized(self):
        """Test capitalize string already capitalized"""
        self.assertEqual(self.processor.capitalize_string("Hello"), "Hello")

    def test_capitalize_string_empty(self):
        """Test capitalize string empty"""
        self.assertEqual(self.processor.capitalize_string(""), "")

    def test_capitalize_string_with_numbers(self):
        """Test capitalize string with numbers"""
        self.assertEqual(self.processor.capitalize_string("123abc"), "123abc")

    def test_count_vowels_normal(self):
        """Test count vowels"""
        self.assertEqual(self.processor.count_vowels("привіт"), 2)

    def test_count_vowels_mixed_case(self):
        """Test count vowels with mixed case"""
        self.assertEqual(self.processor.count_vowels("Привіт"), 2)

    def test_count_vowels_empty(self):
        """Test count vowels with empty string"""
        self.assertEqual(self.processor.count_vowels(""), 0)

    def test_count_vowels_with_numbers_and_symbols(self):
        """Test count vowels with numbers and symbols"""
        self.assertEqual(self.processor.count_vowels("При3віт!"), 0)


if __name__ == "__main__":
    unittest.main()
