from src.expense import Expense
from src.file_handler import save_expense
from src.reports import total_expense, category_wise_report


def show_menu():
    print("\n--- Personal Expense Manager ---")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. View Category Report")
    print("4. Exit")


def handle_user_choice(choice):
    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        description = input("Description: ")

        expense = Expense(date, category, amount, description)
        save_expense(expense)
        print("Expense added successfully!")

    elif choice == "2":
        print("Total Expense:", total_expense())

    elif choice == "3":
        report = category_wise_report()
        for cat, amt in report.items():
            print(f"{cat}: {amt}")

    elif choice == "4":
        print("Exiting...")
        return False

    else:
        print("Invalid choice")

    return True
