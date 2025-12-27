import unittest
import os
from src.file_handler import save_expense
from src.expense import Expense
from src.reports import total_expense, category_wise_report
from src.constants import DATA_FILE_PATH


class TestReports(unittest.TestCase):

    def setUp(self):
        if os.path.exists(DATA_FILE_PATH):
            os.rename(DATA_FILE_PATH, DATA_FILE_PATH + ".bak")

        save_expense(Expense("2025-01-01", "Food", 100))
        save_expense(Expense("2025-01-02", "Food", 200))
        save_expense(Expense("2025-01-03", "Transport", 50))

    def tearDown(self):
        if os.path.exists(DATA_FILE_PATH):
            os.remove(DATA_FILE_PATH)
        if os.path.exists(DATA_FILE_PATH + ".bak"):
            os.rename(DATA_FILE_PATH + ".bak", DATA_FILE_PATH)

    def test_total_expense(self):
        self.assertEqual(total_expense(), 350)

    def test_category_wise_report(self):
        report = category_wise_report()
        self.assertEqual(report["Food"], 300)
        self.assertEqual(report["Transport"], 50)
