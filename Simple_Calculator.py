import os

# ANSI Colors
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"


history = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    clear_screen()
    print(f"{CYAN}{'=' * 50}")
    print("         SIMPLE CALCULATOR")
    print(f"{'=' * 50}{RESET}")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{RED}❌ Invalid input. Enter a valid number.{RESET}")


def show_menu():
    print(f"""
{YELLOW}Choose an operation:{RESET}

  [1] ➕ Addition
  [2] ➖ Subtraction
  [3] ✖ Multiplication
  [4] ➗ Division
  [5] 📜 View History
  [6] 🚪 Exit
""")


def calculate(choice, num1, num2):
    if choice == "1":
        return num1 + num2, "+"
    elif choice == "2":
        return num1 - num2, "-"
    elif choice == "3":
        return num1 * num2, "*"
    elif choice == "4":
        if num2 == 0:
            return None, "/"
        return num1 / num2, "/"


def show_history():
    print(f"\n{MAGENTA}{'-' * 50}")
    print("CALCULATION HISTORY")
    print(f"{'-' * 50}{RESET}")

    if not history:
        print("No calculations yet.")
    else:
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item}")

    input("\nPress Enter to continue...")


def main():
    while True:
        header()
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print(f"\n{GREEN}Thank you for using Simple Calculator! 👋{RESET}")
            break

        if choice == "5":
            show_history()
            continue

        if choice not in ["1", "2", "3", "4"]:
            print(f"\n{RED}❌ Invalid choice! Please select 1-6.{RESET}")
            input("Press Enter to continue...")
            continue

        print(f"\n{CYAN}Enter Numbers{RESET}")
        num1 = get_number("First Number  : ")
        num2 = get_number("Second Number : ")

        result, symbol = calculate(choice, num1, num2)

        if result is None:
            print(f"\n{RED}❌ Error: Cannot divide by zero!{RESET}")
        else:
            expression = f"{num1} {symbol} {num2} = {result}"
            history.append(expression)

            print(f"\n{GREEN}{'=' * 50}")
            print("RESULT")
            print(f"{'=' * 50}")
            print(f"{expression}")
            print(f"{'=' * 50}{RESET}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()