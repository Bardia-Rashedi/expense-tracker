def show_menu():
    print("1. Add expense")
    print("2. View expenses")
    print("3. See total")
    print("4. Quit")

expenses=[]

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What was it for? ")
        amount = float(input("How much? "))
        expenses.append((description, amount))
        print("Added!")    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        for description, amount in expenses:
            print(f"{description}: £{amount:.2f}")
    elif choice == "3":
        total = sum(amount for description, amount in expenses)
        print(f"Total: £{total:.2f}")
    elif choice == "3":
        print("You chose: See total")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")