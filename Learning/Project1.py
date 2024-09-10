
# Create a new account.
# Deposit money.
# Withdraw money.
# Check balance.
# Transfer money to another account.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"NRP {amount} added successfully!")
        else:
            print("Invalid amount!!")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        else:
            self.balance -= amount
            print("Withdraw successful!")
    
    def display_balance(self):
        print(f"NRP {self.balance}")
    
    def transfer(self, amount, another_account):
        if amount > self.balance:
            print("Insufficient balance for transfer.")
        elif amount <= 0:
            print("Transfer amount must be greater than zero.")
        else:
            self.balance -= amount
            another_account.balance += amount
            print(f"Transferred {amount} to account {another_account.account_number}. New balance: {self.balance}")
    

account1 = BankAccount(1, "Rabin", 1000)
account2 = BankAccount(2, "Reejan", 2000)

#Examples
account1.deposit(100)
account1.transfer(50,account2)
