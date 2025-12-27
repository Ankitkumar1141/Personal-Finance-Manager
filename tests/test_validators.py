import unittest
from src.validators import validate_date, validate_amount, validate_category


class TestValidators(unittest.TestCase):

    def test_validate_date_valid(self):
        self.assertTrue(validate_date("2025-01-01"))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date("01-01-2025"))

    def test_validate_amount_valid(self):
        self.assertTrue(validate_amount(100))

    def test_validate_amount_invalid(self):
        self.assertFalse(validate_amount(-50))

    def test_validate_category_valid(self):
        self.assertTrue(validate_category("Food"))

    def test_validate_category_invalid(self):
        self.assertFalse(validate_category(""))
