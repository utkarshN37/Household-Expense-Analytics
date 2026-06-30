# Import csv module to work with CSV files
import csv

# List to store expenses while program is running
total_expense = []


# -------------------------
# Load old expenses from CSV
# -------------------------
def load_expenses():

    try:
        # Open CSV file in read mode
        with open("expenses.csv", "r", newline="") as file:

            # Create CSV reader object
            reader = csv.reader(file)

            # Read each row one by one
            for row in reader:

                # Skip empty rows
                if len(row) == 0:
                    continue

                # Convert row into dictionary
                expense = {
                    "category": row[0],
                    "amount": int(row[1])
                }

                # Add dictionary to list
                total_expense.append(expense)

    # If file doesn't exist yet, ignore the error
    except FileNotFoundError:
        pass


# -------------------------
# Add a new expense
# -------------------------
def add_expense():

    category = input("Enter category : ")

    # Handle invalid amount input
    try:
        amount = int(input("Enter amount : "))

    except ValueError:
        print("Please enter a valid number.")
        return

    # Create dictionary
    expense = {
        "category": category,
        "amount": amount
    }

    # Store in RAM
    total_expense.append(expense)

    # Store permanently in CSV file
    with open("expenses.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            expense["category"],
            expense["amount"]
        ])

    print("Expense added successfully!")


# -------------------------
# View all expenses
# -------------------------
def view_expenses():

    if len(total_expense) == 0:
        print("No expenses found.")

    else:

        for expense in total_expense:

            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']}")
            print("-" * 20)


# -------------------------
# Show total spending
# -------------------------
def show_total():

    if len(total_expense) == 0:
        print("No expenses found.")
        return

    total = 0

    for expense in total_expense:
        total += expense["amount"]

    print(f"TOTAL SPENDING : ₹{total}")


# Load previous expenses before starting menu
load_expenses()


# -------------------------
# Main Menu
# -------------------------
while True:

    print("\n======= Expense Tracker =======")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Exit")

    choice = input("Choose option : ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("INVALID CHOICE")