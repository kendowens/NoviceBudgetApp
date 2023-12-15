import tkinter as tk
from my_budget import Budget, Transaction

def add_income():
    date = date_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())
    income = Transaction(date, description, amount)
    my_budget.add_income(income)
    status_label.config(text="Income added successfully!")

def add_expense():
    date = date_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())
    expense = Transaction(date,description,amount)
    my_budget.add_expense(expense)
    status_label.config(text="Expense added successfully!")

def show_transaction():
    transactions = "\nTransactions:\n"
    for transaction in my_budget.incomes + my_budget.expenses:
        transactions += f"{transaction.date} - {transaction.description}: ${transaction.amount}\n"
        status_label.config(text=transactions)

def calculate_balance():
    balance = f"\nCurrent Balance: ${my_budget.calculate_balance()}"
    status_label.config(text=balance)

def exit_app():
    root.destroy()

my_budget = Budget()

root = tk.Tk()
root.title("Budgeting App")

#create entry fields and buttons

date_label = tk.Label(root, text = "Date (YYYY-DD-MM): ")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

description_label = tk.Label(root, text = "Description: ")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

amount_label = tk.Label(root, text = "Amount : ")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

add_income_button = tk.Button(root, text = "Add Income", command = add_income)
add_income_button.pack()

add_expense_button = tk.Button(root, text = "Add Expense", command = add_expense)
add_expense_button.pack()

show_transactions_button = tk.Button(root, text = "Show Transactions", command = show_transaction)
show_transactions_button.pack()

calculate_balance_button = tk.Button(root, text = "Calculate Balance", command = calculate_balance)
calculate_balance_button.pack()

exit_button = tk.Button(root, text = "Exit", command = exit_app)
exit_button.pack()

status_label = tk.Label(root, text = "")
status_label.pack()

root.mainloop()