import file_handler
import ui

def main():
    expenses = file_handler.load_expenses()

    while True:
        print("\n--- PERSONAL FINANCE MANAGER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Reports")
        print("4. Backup")
        print("5. Restore")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            ui.add_expense_ui(expenses)
        elif choice == "2":
            ui.view_expenses_ui(expenses)
        elif choice == "3":
            ui.reports_ui(expenses)
        elif choice == "4":
            file_handler.backup_data()
            print("Backup completed.")
        elif choice == "5":
            file_handler.restore_data()
            expenses = file_handler.load_expenses()
            print("Data restored.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
