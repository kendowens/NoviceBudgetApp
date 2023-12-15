from my_budget import Budget, Transaction #import Transaction and budget class from my_budget

#function to display menu

def display_menu():
    print ("\nBudgeting App Menu")
    print ("1. Add Income")
    print ("2. Add Expense")
    print ("3. Show Transactions")
    print ("4. Calculate Balance")
    print ("5. Exit")

#Main Program Loop
def main():
    my_budget = Budget() #instance of Budget class

    while True :
        display_menu()
        choice = input ("Enter your choice (1-5): ")

        if choice == "1":
        #add income
            date = input("Enter Date YYYY-DD-MM: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            income = Transaction(date, description, amount)
            my_budget.add_income(income)
            print("Income added successfully!")

        elif choice == "2":
        #add expense
            date = input("Enter Date YYYY-DD-MM: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense = Transaction(date, description, amount)
            my_budget.add_expense(expense)

        elif choice == "3":
        #show transactions
            print("\nTransactions:")
            for transaction in my_budget.incomes + my_budget.expenses:
                print(f"{transaction.date} - {transaction.description}: ${transaction.amount}")

        elif choice == "4":
            #calculate balance
            print(f"\nCurrent Balance: ${my_budget.calculate_balance()}")

        elif choice == "5":
            #exit program
            print("Exiting Program, Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1 through 5")

if __name__ == "__main__":
    main()