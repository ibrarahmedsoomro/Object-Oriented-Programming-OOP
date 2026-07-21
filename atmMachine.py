class BankAccount:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def login(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            print(f"\nWelcome {self.name}!")
            self.menu()
        else:
            print("Incorrect PIN!")

    def check_balance(self):
        print(f"Your Balance: Rs. {self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            print("Deposit Successful!")
            self.check_balance()
        else:
            print("Invalid Amount!")

    def withdraw(self):
        amount = float(input("Enter withdraw amount: "))

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            self.check_balance()
        else:
            print("Insufficient Balance!")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN Changed Successfully!")
        else:
            print("Wrong Old PIN!")

    def menu(self):
        while True:
            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.change_pin()

            elif choice == "5":
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid Choice!")


# Object Creation
account = BankAccount("Ibrar", "1234", 5000)

# Start ATM
account.login()