import os
from tkinter import filedialog
import json
from my_budget import Transaction, Budget

my_budget = Budget()

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