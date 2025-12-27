import csv
import os
from expense import Expense
from constants import EXPENSE_FILE, BACKUP_FILE

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for e in expenses:
            writer.writerow(e.to_list())


def load_expenses():
    expenses = []
    if not os.path.exists(EXPENSE_FILE):
        return expenses

    with open(EXPENSE_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(
                Expense(
                    row["Amount"],
                    row["Category"],
                    row["Date"],
                    row["Description"]
                )
            )
    return expenses


def backup_data():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as src, open(BACKUP_FILE, "w") as dst:
            dst.write(src.read())


def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r") as src, open(EXPENSE_FILE, "w") as dst:
            dst.write(src.read())
