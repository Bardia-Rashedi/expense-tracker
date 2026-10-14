def show_menu():
    print("1. Add expense")
    print("2. View expenses")
    print("3. See total")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        print("You chose: Add expense")
    elif choice == "2":
        print("You chose: View expenses")
    elif choice == "3":
        print("You chose: See total")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")