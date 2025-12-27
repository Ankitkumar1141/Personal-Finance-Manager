import csv
import os
from src.constants import CSV_HEADERS, DATA_FILE_PATH
from src.expense import Expense


def initialize_file():
    os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)

    if not os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
            writer.writeheader()


def save_expense(expense: Expense):
    initialize_file()
    with open(DATA_FILE_PATH, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writerow(expense.to_dict())


def load_expenses():
    initialize_file()
    expenses = []

    with open(DATA_FILE_PATH, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Normalize keys to lowercase
            row = {k.strip().lower(): v for k, v in row.items()}

            expenses.append(
                Expense(
                    row["date"],
                    row["category"],
                    float(row["amount"]),
                    row.get("description", "")
                )
            )

    return expenses
