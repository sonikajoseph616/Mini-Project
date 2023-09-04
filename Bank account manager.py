from abc import ABC, abstractmethod

class Account(ABC):
    def _init_(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def _init_(self, balance=0):
        super()._init_(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def _init_(self, balance=0):
        super()._init_(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

class BusinessAccount(Account):
    def _init_(self, balance=0):
        super()._init_(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

def main():
    checking = CheckingAccount(1000)
    savings = SavingsAccount(5000)
    business = BusinessAccount(10000)

    while True:
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Business Account")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter your choice: "))
            amount = float(input("Enter amount: "))
            if ch == 1:
                checking.deposit(amount)
            elif ch == 2:
                checking.withdraw(amount)
        elif choice == 2:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter your choice: "))
            amount = float(input("Enter amount: "))
            if ch == 1:
                savings.deposit(amount)
            elif ch == 2:
                savings.withdraw(amount)
        elif choice == 3:
            print("1. Deposit")
            print("2. Withdraw")
            ch = int(input("Enter your choice: "))
            amount = float(input("Enter amount: "))
            if ch == 1:
                business.deposit(amount)
            elif ch == 2:
                business.withdraw(amount)
        elif choice == 4:
            break

if _name_ == "_main_":
    main()
