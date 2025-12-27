import unittest
from src.expense import Expense


class TestExpense(unittest.TestCase):

    def test_expense_creation_success(self):
        expense = Expense("2025-01-01", "Food", 100, "Lunch")
        self.assertEqual(expense.amount, 100)

    def test_expense_invalid_date(self):
        with self.assertRaises(ValueError):
            Expense("01-01-2025", "Food", 100)

    def test_expense_invalid_amount(self):
        with self.assertRaises(ValueError):
            Expense("2025-01-01", "Food", -100)

    def test_expense_invalid_category(self):
        with self.assertRaises(ValueError):
            Expense("2025-01-01", "", 100)
