import tkinter as tk
from tkinter import filedialog
import json
from my_budget import Transaction, Budget
import os

#create an instance of the Budget class
my_budget = Budget()

#define GUI functions here

def add_income():
    #get data from the entry fields and create Transaction object
    date = date_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())
    income = Transaction(date, description, amount)

    #call the Budget class method to add income
    my_budget.add_income(income)
    status_label.config(text="Income added successfully!")
    save_budget_data()

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

#persistence and save location

def get_default_save_path():
    return os.path.join(os.path.expanduser('~'), 'BudgetApp', 'budget_app.json')

def save_budget_data(budget_user_data=None):
    if not budget_user_data:
        budget_user_data = get_default_save_path()

    data = {
        "incomes": [vars(income) for income in my_budget.incomes],
        "expenses": [vars(expense) for expense in my_budget.expenses],
        "balances": my_budget.calculate_balance()
    }

    with open(budget_user_data, 'w') as file:
        json.dump(data, file)

def load_budget_data(budget_user_data=None):
    if not budget_user_data:
        budget_user_data = get_default_save_path()

    with open(budget_user_data, 'r') as file:
        data = json.load(file)

    my_budget.incomes = [Transaction(**income) for income in data["incomes"]]
    my_budget.expenses = [Transaction(**expense) for expense in data["expenses"]]
    my_budget.balances = data["balances"]

def ask_for_save_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".json",
                                             filetypes=[("JSON files", "*.json")])
    return save_path

user_choice = input("Do you want to use the default save path? (y/n): ")
if user_choice.lower() == 'n':
    file_path = ask_for_save_path()
    save_budget_data(file_path)
else:
    save_budget_data()
load_budget_data()

#dialog and GUI

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