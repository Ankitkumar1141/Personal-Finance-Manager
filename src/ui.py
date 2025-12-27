from expense import Expense
import file_handler
import reports
from validators import validate_amount, validate_date

def add_expense_ui(expenses):
    try:
        amount = float(input("Enter amount: "))
        if not validate_amount(amount):
            print("Invalid amount.")
            return

        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        if not validate_date(date):
            print("Invalid date format.")
            return

        description = input("Enter description: ")

        expenses.append(Expense(amount, category, date, description))
        file_handler.save_expenses(expenses)
        print("Expense added successfully.")

    except ValueError:
        print("Invalid input.")


def view_expenses_ui(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for e in expenses:
        print(e)


def reports_ui(expenses):
    print("\nTotal Expense:", reports.total_expenses(expenses))
    print("Average Expense:", reports.average_expense(expenses))
    print("\nCategory-wise Summary:")
    for cat, amt in reports.category_wise_summary(expenses).items():
        print(f"{cat}: {amt:.2f}")
