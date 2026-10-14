import csv

FILE_NAME = "expenses.csv"
def show_menu():

    print("1. Add expense")
    print("2. View expenses")
    print("3. See total")
    print("4. Quit")
def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, newline="") as file:
            for row in csv.reader(file):
                expenses.append((row[0], float(row[1])))
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

expenses=load_expenses()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What was it for? ")
        try:
            amount = float(input("How much? "))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue
        expenses.append((description, amount))
        save_expenses(expenses)
        print("Added!")    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        for description, amount in expenses:
            print(f"{description}: £{amount:.2f}")
    elif choice == "3":
        total = sum(amount for description, amount in expenses)
        print(f"Total: £{total:.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")