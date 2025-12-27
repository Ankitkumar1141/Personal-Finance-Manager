# Personal Finance Management System (CLI)

## 📌 Project Overview

The **Personal Finance Management System** is a command-line based Python application designed to help users **track expenses, manage financial data, generate reports, and analyze spending patterns**.

The project follows **professional software quality standards**, including:
- Modular architecture
- Object-Oriented Design
- CSV-based data persistence
- Input validation and error handling
- Automated testing
- Clear documentation

This project is suitable for **academic submissions, lab exams, training programs, and beginner-to-intermediate Python portfolios**.

---

## 🎯 Features

- Add and store expenses (amount, category, date, description)
- Persist data using CSV files
- View all recorded expenses
- Generate financial reports:
  - Total expenses
  - Average expenses
  - Category-wise expense summary
- Backup and restore expense data
- Input validation and formatted output
- Automated unit testing for reliability

---

## 🗂️ Project Structure

```
personal_finance_manager/
│
├── expense.py
├── file_handler.py
├── reports.py
├── ui.py
├── validators.py
├── constants.py
├── main.py
│
├── expenses.csv
│
├── tests/
│   ├── test_expense.py
│   ├── test_validators.py
│   ├── test_reports.py
│   └── test_file_handler.py
│
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8 or higher
- No external libraries required

---

## 🚀 Setup Instructions

### 1️⃣ Ensure `expenses.csv` Exists

Create a file named **expenses.csv** in the project root with the following sample data:

```csv
Date,Category,Amount,Description
2025-01-01,Food,250,Lunch
2025-01-02,Transport,120,Bus fare
2025-01-03,Shopping,1500,Clothes
```

---

### 2️⃣ Run the Application

```bash
python main.py
```

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## ✅ Quality Standards Compliance

- Modular design
- Input validation
- Error handling
- Persistent storage
- Automated testing
- Documentation

---

## 👤 Author

Ankit Kumar Jha