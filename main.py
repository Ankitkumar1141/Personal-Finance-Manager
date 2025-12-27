from src.ui import show_menu, handle_user_choice


def main():
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice: ")
        running = handle_user_choice(choice)


if __name__ == "__main__":
    main()
