balance = 10000
daily_limit = 5000
withdrawn = 0

while True:
    print("\n1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        elif withdrawn + amount > daily_limit:
            print("Daily limit exceeded.")
        else:
            balance -= amount
            withdrawn += amount
            print("Withdrawal successful.")
            print("Balance:", balance)
            print("Remaining daily limit:", daily_limit - withdrawn)

    elif choice == "2":
        print("Balance:", balance)
        print("Remaining daily limit:", daily_limit - withdrawn)

    elif choice == "3":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice.")
