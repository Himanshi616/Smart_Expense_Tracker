expenses = []

print("SMART EXPENSE TRACKER")


def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    expense = [date, category, description, amount]
    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        for i in range(len(expenses)):
            print("\nExpense", i + 1)
            print("Date:", expenses[i][0])
            print("Category:", expenses[i][1])
            print("Description:", expenses[i][2])
            print("Amount: Rs.", expenses[i][3])


def expense_analysis():
    print("\n--- Expense Analysis ---")

    if len(expenses) == 0:
        print("No expenses available.")
    else:
        total = 0

        for expense in expenses:
            total = total + expense[3]

        average = total / len(expenses)

        print("Total Expense: Rs.", total)
        print("Average Expense: Rs.", average)


def budget_management():
    print("\n--- Budget Management ---")

    budget = float(input("Enter your budget: "))

    total = 0

    for expense in expenses:
        total = total + expense[3]

    remaining = budget - total

    print("Budget: Rs.", budget)
    print("Total Expense: Rs.", total)

    if remaining >= 0:
        print("Remaining Budget: Rs.", remaining)
    else:
        print("Budget exceeded by: Rs.", -remaining)


while True:
    print("\nSMART EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Budget Management")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        expense_analysis()

    elif choice == "4":
        budget_management()

    elif choice == "5":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
