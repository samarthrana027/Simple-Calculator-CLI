# Simple Calculator CLI

A colorful and interactive command-line calculator application built with Python. This calculator provides basic arithmetic operations with a user-friendly interface, calculation history tracking, and colored terminal output.

## Features

✨ **Core Features:**
- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract two numbers
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide two numbers (with zero-division protection)
- 📜 **View History** - Keep track of all calculations performed
- 🎨 **Colored Output** - Beautiful ANSI colored terminal interface
- ✅ **Input Validation** - Robust error handling for invalid inputs

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/samarthrana027/synent-task1-Simple-Calculator-CLI--Samarth.git
cd synent-task1-Simple-Calculator-CLI--Samarth
```

2. Ensure Python is installed on your system:
```bash
python --version
```

## Usage

Run the calculator:
```bash
python Simple_Calculator.py
```

### How to Use

1. The calculator will display a menu with 6 options
2. Enter your choice (1-6):
   - **1** - Addition
   - **2** - Subtraction
   - **3** - Multiplication
   - **4** - Division
   - **5** - View Calculation History
   - **6** - Exit the calculator

3. Enter the first and second numbers when prompted
4. The result will be displayed with the calculation expression
5. Your calculation is automatically saved to history
6. Press Enter to return to the main menu

### Example Session

```
==================================================
         SIMPLE CALCULATOR
==================================================

Choose an operation:

  [1] ➕ Addition
  [2] ➖ Subtraction
  [3] ✖ Multiplication
  [4] ➗ Division
  [5] 📜 View History
  [6] 🚪 Exit

Enter your choice (1-6): 1

Enter Numbers
First Number  : 10
Second Number : 5

==================================================
RESULT
==================================================
10.0 + 5.0 = 15.0
==================================================

Press Enter to continue...
```

## Features Explained

### 🎨 Color Scheme
- **CYAN** - Headers and prompts
- **GREEN** - Successful results and exit messages
- **YELLOW** - Menu options
- **RED** - Error messages and validation alerts
- **MAGENTA** - Calculation history

### 📋 Calculation History
All calculations are stored in memory and can be viewed at any time by selecting option 5. The history persists until the program exits.

### ❌ Error Handling
- **Invalid Input** - Non-numeric inputs are caught and re-prompted
- **Division by Zero** - Protected with error message and no calculation recorded
- **Invalid Choice** - Non-existent menu options are rejected with guidance

## Code Structure

- **`clear_screen()`** - Clears the terminal screen (cross-platform compatible)
- **`header()`** - Displays the application header
- **`get_number(prompt)`** - Safely gets numeric input with validation
- **`show_menu()`** - Displays the operation menu
- **`calculate(choice, num1, num2)`** - Performs the calculation based on user choice
- **`show_history()`** - Displays all previous calculations
- **`main()`** - Main application loop

## Platform Compatibility

✅ **Works on:**
- Windows
- macOS
- Linux

The script uses cross-platform commands for clearing the screen.

## Future Enhancements

Potential improvements for future versions:
- Save calculation history to a file
- Support for more operations (power, square root, modulo, etc.)
- Keyboard shortcuts
- Dark/Light theme toggle
- Calculation history search/filter

## License

This project is open source and available for educational purposes.

## Author

**Samarth Rana** - samarthrana027

---

Made with ❤️ for learning Python CLI applications
