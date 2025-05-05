'''Q.4)Bank Account Simulation
Create a class BankAccount with deposit, withdraw, and check balance functionalities.
Prevent withdrawal if balance is insufficient.'''
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.balance)

# Example usage
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.check_balance()
