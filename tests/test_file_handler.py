import unittest
import os
from src.file_handler import save_expense, load_expenses
from src.expense import Expense
from src.constants import DATA_FILE_PATH


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Backup existing file
        if os.path.exists(DATA_FILE_PATH):
            os.rename(DATA_FILE_PATH, DATA_FILE_PATH + ".bak")

    def tearDown(self):
        # Restore backup
        if os.path.exists(DATA_FILE_PATH):
            os.remove(DATA_FILE_PATH)
        if os.path.exists(DATA_FILE_PATH + ".bak"):
            os.rename(DATA_FILE_PATH + ".bak", DATA_FILE_PATH)

    def test_save_and_load_expense(self):
        expense = Expense("2025-01-01", "Food", 200, "Dinner")
        save_expense(expense)

        expenses = load_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].category, "Food")
