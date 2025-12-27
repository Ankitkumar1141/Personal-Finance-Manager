from collections import defaultdict

def total_expenses(expenses):
    return sum(e.amount for e in expenses)

def average_expense(expenses):
    return total_expenses(expenses) / len(expenses) if expenses else 0

def category_wise_summary(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return summary
