"""
Bank Accounts I - Opening An Account
"""

# Create an "Account" class to represent unique bank accounts. Ensure that when you create a new instance of Account, that instances has attributes for the bank account number, account owner's name, and the initial balance. It should have a class attribute for the default interest rate on a general account. Add an instance method called "acc_details" that prints out all these account details. Then create at least once instance and print out its details.

class Account():
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.acc_num = account_number
        self.balance = initial_amount

    int_rate = 0.5

    def acc_details(self):
        print(f'Account No.: {self.acc_num}\nAccount Holder: {self.name}\nInterest Rate: {self.int_rate}\nBalance: ${self.balance}\n')


alejandra = Account('Alejandra Ochoa', '554951', 20000)