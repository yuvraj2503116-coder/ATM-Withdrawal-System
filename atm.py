class ATMAccount:
    def __init__(self, balance=10000, daily_limit=5000):
        self.balance = balance
        self.daily_limit = daily_limit
        self.withdrawn_today = 0

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."

        remaining_limit = self.daily_limit - self.withdrawn_today

        if amount > remaining_limit:
            return "Daily withdrawal limit exceeded."

        if amount > self.balance:
            return "Insufficient balance."

        self.balance -= amount
        self.withdrawn_today += amount

        return "Withdrawal successful."

    def check_balance(self):
        return self.balance

    def remaining_daily_limit(self):
        return self.daily_limit - self.withdrawn_today


def main():
    account = ATMAccount()

    while True:
        print("\n===== ATM SYSTEM =====")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter withdrawal amount: "))

                message = account.withdraw(amount)
                print(message)

                if message == "Withdrawal successful.":
                    print(f"Remaining balance: ₹{account.balance:.2f}")
                    print(
                        f"Remaining daily limit: "
                        f"₹{account.remaining_daily_limit():.2f}"
                    )

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            print(f"Current balance: ₹{account.check_balance():.2f}")
            print(
                f"Remaining daily limit: "
                f"₹{account.remaining_daily_limit():.2f}"
            )

        elif choice == "3":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
