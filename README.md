# Expense Tracker

A simple command-line expense tracker written in Python. Add your expenses, view them, and see the running total. Everything is saved to a CSV file, so your data is still there next time you open it.

## Features

- Add an expense with a description and amount
- View all saved expenses
- See the total spent
- Rejects invalid amounts (like letters) instead of crashing
- Saves expenses to `expenses.csv` automatically after each one is added

## How to run

You need Python 3 installed.

```
git clone https://github.com/Bardia-Rashedi/expense-tracker.git
cd expense-tracker
python expenses.py
```

## Example

```
1. Add expense
2. View expenses
3. See total
4. Quit
Choose an option: 1
What was it for? Lunch
How much? 8.50
Added!
Choose an option: 3
Total: £8.50
```

## What I learned

- Structuring a program with functions and a main loop
- Reading and writing CSV files with Python's `csv` module
- Handling bad user input with `try` / `except`
- Using Git and GitHub to track changes step by step