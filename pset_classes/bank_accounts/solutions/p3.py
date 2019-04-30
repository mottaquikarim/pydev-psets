"""
Bank Accounts III - Savings Accounts
"""

# Create a "SavingsAccount" class that inherits from the general Account class. It should have its own "int_rate" as a class attribute. Create at least once instance of SavingsAccount and call both the deposit() method from its parent class on it.

class Account():
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.acc_num = account_number
        self.balance = initial_amount
        self.transactions = {}

    int_rate = 0.5
    
    def acc_details(self):
        print(f'Account No.: {self.acc_num}\nAccount Holder: {self.name}\nInterest Rate: {self.int_rate}\nBalance: ${self.balance}\n')

    def deposit(self, amount):
        start_amount = self.balance
        self.balance += amount
        end_amount = self.balance
        label = 'Deposit'
        self.transactions.update({label: [start_amount, end_amount]})
        print(f'${amount} deposit complete.')


class SavingsAccount(Account):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.acc_num = account_number
        self.balance = initial_amount
        self.transactions = {}

    int_rate = 2.1


priya = SavingsAccount('Priya Ghadiya', 488812, 2500)

priya.deposit(1500)
print(f'${priya.balance}') # 4000
print(priya.transactions) # {'Deposit': [2500, 4000]}

priya.acc_details()