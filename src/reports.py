from collections import defaultdict
from src.file_handler import load_expenses


def total_expense():
    expenses = load_expenses()
    return sum(exp.amount for exp in expenses)


def category_wise_report():
    expenses = load_expenses()
    report = defaultdict(float)

    for exp in expenses:
        report[exp.category] += exp.amount

    return dict(report)
