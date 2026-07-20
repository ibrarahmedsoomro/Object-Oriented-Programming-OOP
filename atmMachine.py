class BankAcc:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def login(self):
        user_pin = input("Enter Your Pin: ")
        
        if user_pin == self.pin:
            print(f"\n Welcome to NBP ATM MACHINE {self.name}!")
            self.menu()
        else:
            print("Invalid Pin")
    def checkBalance(self):
        print(f"Your Balance is Rs.{self.balance}")

    def deposit(self):
        amount = float("Enter your deposit amount:")

        if amount>0:
            self.balance += amount
            print("Amount added sucessfuly")
            self.checkBalance()
        else:
            print("Please Enter a valid amount")

    def withdraw(self):
        amount = float("Enter a amount:")
        if amount >0:
            print(f"You balance is deducted")
            self.balance -= amount
            self.checkBalance()
        else:
            print("Enter a valid balance")
    
    def changePin(self):
        oldpin = input("Enter a Old Pin")

        if oldpin == self.pin:
            newpin = input("Enter a new pin")
            self.pin = newpin
            print("Pin Created Sucessfully")
        else:
            print("Enter a Correct Pin")
    
    def menu(self):
        while True:
            print("\n======ATM MENU======") 
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change Pin")
            print("5. Exit")

            choice = input("Enter your Choice")

            if choice == "1":
                self.checkbalace()
    
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.changePin()
            elif choice == "5":
                print("Thank You for using atm machine")
                break
            else:
                print("Invalid Choice")


acc = BankAcc("Ibrar", 3322, 32222)

acc.login()