"""
Bank Accounts IV - Checking Accounts
"""

# Create a "CheckingAccount" class that inherits from the general Account class. It should have its own "int_rate" as a class attribute and a "withdraw" instance method. The latter should work the same as the "deposit()" method in the parent class. Create at least once instance of CheckingAccount and call both the deposit and withdraw() methods on it.

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


class CheckingAccount(Account):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.acc_num = account_number
        self.balance = initial_amount
        self.transactions = {}

    int_rate = 1.3

    def withdraw(self, amount):
        start_amount = self.balance
        self.balance -= amount
        end_amount = self.balance
        label = 'Withdrawal'
        self.transactions.update({label: [start_amount, end_amount]})
        print(f'${amount} withdrawal complete.')


brad = CheckingAccount('Brad Fenwick', 239055, 5000)

brad.deposit(1000)
print(f'${brad.balance}') # 6000

brad.withdraw(250)
print(f'${brad.balance}') # 5750

print(brad.transactions) # {'Deposit': [5000, 6000], 'Withdrawal': [6000, 5750]}

brad.acc_details()