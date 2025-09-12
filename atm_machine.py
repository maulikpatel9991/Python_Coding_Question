"""
ATM Simulation in Python

Problem Statement:
-------------------
Design a simple ATM system that allows users to:
1. Verify PIN
2. Check account balance
3. Withdraw money
4. Deposit money
5. Exit the system

Features:
---------
- PIN verification is required before any transaction
- Input validation for withdrawal and deposit
- Prevents negative or invalid transactions
- Proper error handling and user-friendly messages

Author: [Your Name]
Date: [Date of Submission or Today’s Date]
"""

# ATM class implementation starts below

class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.pin_verified = False

    def check_balance(self):
        print(f"\n💰 Your current balance is: ₹{self.balance}\n")

    def withdraw(self):
        try:
            amount = int(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                raise ValueError("Please enter a positive amount.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        except ValueError as error:
            print(f"❌ {error}")

    def deposit(self):
        try:
            amount = int(input("Enter deposit amount: ₹"))
            if amount <= 0:
                raise ValueError("Please enter a positive amount.")
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        except ValueError as error:
            print(f"❌ {error}")

    def verify_pin(self):
        try:
            pin_input = input("Enter PIN: ")
            if pin_input == "7689":
                self.pin_verified = True
                print("🔓 PIN verified successfully.")
            else:
                raise ValueError("Invalid PIN.")
        except ValueError as error:
            print(f"❌ {error}")

    def menu(self):
        while True:
            try:
                print("\n===== ATM Menu =====")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Verify PIN")
                print("5. Exit")
                choice = int(input("Select an option (1-5): "))

                if choice == 5:
                    print("👋 Thank you for using the ATM.")
                    break

                # Allow only verifying PIN first before any action
                if not self.pin_verified and choice not in [4, 5]:
                    print(not self.pin_verified)
                    print("🔐 Please verify your PIN first.")
                    continue

                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.withdraw()
                elif choice == 3:
                    self.deposit()
                elif choice == 4:
                    self.verify_pin()
                else:
                    print("❌ Invalid selection. Please choose a number from 1 to 5.")

            except ValueError:
                print("❌ Invalid input. Please enter a number.")

if __name__ == '__main__':
    atm = ATM(initial_balance=1000)
    atm.menu()
