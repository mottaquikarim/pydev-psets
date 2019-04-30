"""
Bank Accounts V - Transfer Money
"""

# Create a method called "acc_transfer" within the Account class. This should deduct money from the account and deposit it some another account. Ensure the outgoing money transfer gets recorded as an outgoing transaction in the giving account. It should get recorded as a deposit in the receiving account. Call this method and check the final balances and transactions of both the giving and receiving accounts. 

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

    def acc_transfer(self, amount, target_acc):
        start_amount = self.balance
        self.balance -= amount
        target_acc.deposit(amount)
        end_amount = self.balance
        label = 'Outgoing Transfer'
        self.transactions.update({label: [start_amount, end_amount]})
        print(f'${amount} outgoing transfer complete.')


class SavingsAccount(Account):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.acc_num = account_number
        self.balance = initial_amount
        self.transactions = {}

    int_rate = 2.1

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


priya = SavingsAccount('Priya Ghadiya', 488812, 2500)
alejandra = Account('Alejandra Ochoa', 554951, 20000)

alejandra.acc_transfer(1750, priya)
print(f'${alejandra.balance}')
print(f'${priya.balance}')

print(alejandra.transactions)
print(priya.transactions)