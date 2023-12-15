from my_budget import Transaction, Budget

#test transaction class
def test_transaction():
    #create a transaction
    transaction = Transaction("2023-12-13", "groceries", 100);
    assert transaction.date == "2023-12-13"
    assert transaction.description == "groceries"
    assert transaction.amount == 100
    print ("Transaction class passed")

#test budget class
def test_budget():
    #create a budget instance
    my_budget = Budget()

    #create transaction
    income = Transaction("2023-12-13", "Salary", 3000)
    expense = Transaction("2023-12-13", "Rent", 1000)

    #test adding income and expense to the budget
    my_budget.add_income(income)
    my_budget.add_expense(expense)

    #check if the balance is calculated correctly
    assert my_budget.calculate_balance() == (3000 - 1000)
    print("Budget class test passed")

#Run the tests
if __name__ == "__main__":
    test_transaction()
    test_budget()