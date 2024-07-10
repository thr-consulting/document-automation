import unittest
import re

from amount import MyRegex, txtToAmount


class TestTxtToAmount(unittest.TestCase):

    def setUp(self):
        # Example text for testing
        self.text = """118.58

Total (Includes $12,213.64 HST)

You saved $100,50.00 on this bill

100,127.75

Total to pay

$433.49"""
        self.text1 = """118.58

Total (Includes $12,213.64 HST)

You saved $100,50.00 on this bill

100,127.75

Tota to pay

$433.49"""

        # Define regex patterns for testing
        self.regex_patterns = [
            MyRegex(re.compile(r"total.*total"), 1),
            MyRegex(re.compile(r"(\d*,?\d+\.\d{2}|\d+)"), -2),
        ]

    def test_txtToAmount(self):
        # Call the function with test data
        extracted_amounts = txtToAmount(self.text, self.regex_patterns)

        # Assert expected results
        expected_amounts = 100127.75
        self.assertEqual(extracted_amounts, expected_amounts)

    def test_txtToAmount_None(self):
        # Call the function with test data
        extracted_amounts = txtToAmount(self.text1, self.regex_patterns)

        # Assert expected results
        expected_amounts = None
        self.assertEqual(extracted_amounts, expected_amounts)


if __name__ == "__main__":
    unittest.main()
