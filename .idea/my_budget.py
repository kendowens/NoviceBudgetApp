# define Transaction class
class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

#define the budget class to manage incomes, expenses and balances
class Budget:
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.balances = 0

    def add_income(self, income):
        self.incomes.append(income)
        self.balances += income.amount

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.balances -= expense.amount

    def calculate_balance(self):
        return self.balances


