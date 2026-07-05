# Project Report: Simple Calculator CLI

## 📋 Project Overview
This is a command-line calculator application written in Python that provides basic arithmetic operations with a user-friendly interface. The program features colored output, calculation history tracking, and input validation.

---

## 🎯 Key Features

### 1. **Core Functionality**
- ✅ Addition, Subtraction, Multiplication, and Division operations
- ✅ Input validation for numeric values
- ✅ Error handling for division by zero
- ✅ Calculation history tracking
- ✅ Clean screen interface

### 2. **User Interface**
- **ANSI Color Coding**: Uses colored text for better readability
  - Cyan: Headers and prompts
  - Green: Success messages
  - Yellow: Menu options
  - Red: Error messages
  - Magenta: History section
- **Clear Menu Display**: Emoji icons and formatted options
- **Interactive Prompts**: User-friendly input requests

### 3. **History Management**
- Maintains a list of all calculations performed
- Displays calculations in numbered format
- Persists during the current session

---

## 🏗️ Code Architecture

### **Global Variables**
- `RESET, CYAN, GREEN, YELLOW, RED, MAGENTA`: ANSI color codes
- `history`: List storing calculation records

### **Functions**

| Function | Purpose |
|----------|---------|
| `clear_screen()` | Clears terminal (cross-platform) |
| `header()` | Displays application title and separator |
| `get_number(prompt)` | Validates and retrieves numeric input |
| `show_menu()` | Displays operation options |
| `calculate(choice, num1, num2)` | Performs arithmetic operation |
| `show_history()` | Displays all previous calculations |
| `main()` | Main program loop |

---

## 💡 Code Quality Analysis

### **Strengths**
✅ **Error Handling**: Validates user input and handles division by zero  
✅ **Cross-Platform**: Works on Windows (`cls`) and Unix/Linux (`clear`)  
✅ **User Experience**: Color-coded output and clear prompts  
✅ **Modular Design**: Separated concerns into distinct functions  
✅ **Input Validation**: Loop-based validation for numeric inputs  

### **Potential Improvements**
⚠️ **History Persistence**: History is lost when the program exits (not saved to file)  
⚠️ **Limited Operations**: No power, square root, or modulo operations  
⚠️ **No Undo/Clear History**: No option to clear or manage history  
⚠️ **Float Precision**: May display long decimal results without formatting  
⚠️ **Calculation Feedback**: Could show intermediate steps for complex operations  

---

## 🔄 Program Flow

```
Start Application
    ↓
Display Header & Menu
    ↓
User Selection
    ├─→ [1-4] Perform Calculation → Store in History → Display Result
    ├─→ [5] View History
    └─→ [6] Exit Program
    ↓
Loop or Exit
```

---

## 📊 Technical Specifications

| Aspect | Details |
|--------|---------|
| **Language** | Python 3 |
| **Dependencies** | `os` (standard library) |
| **Platform** | Cross-platform (Windows, Linux, macOS) |
| **Input Method** | Command-line interface |
| **Data Structure** | List (for history) |
| **Error Handling** | Try-except blocks, input validation |

---

## 🚀 Usage Example

```
========================================================
         SIMPLE CALCULATOR
========================================================

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
```

---

## 🎓 Learning Value

This project demonstrates:
- Function definition and modular programming
- Input validation and error handling
- Control flow with loops and conditionals
- String formatting and ANSI color codes
- Cross-platform compatibility
- User interface design principles

---

## 📝 Summary

The **Simple Calculator CLI** is a well-structured beginner-to-intermediate Python project that implements essential calculator functionality with an attractive command-line interface. While it successfully handles core operations, enhancements like persistent history storage and additional mathematical functions would improve its utility for production use.
