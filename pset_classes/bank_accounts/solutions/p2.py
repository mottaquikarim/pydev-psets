"""
Bank Accounts II - Deposit Money
"""

# Write and call a method "deposit()" that allows you to deposit money into the instance of Account. It should update the current account balance, record the transaction in an attribute called "transactions", and prints out a deposit confirmation message.

# Note 1: You can format the transaction records like this - "Deposit: <starting balance>, <ending balance>"
# Note 2: You can format the deposit confirmation message like this - "$<amount> deposit complete."

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



alejandra = Account('Alejandra Ochoa', '554951', 20000)

alejandra.deposit(500)
print(f'${alejandra.balance}')

print(alejandra.transactions)
alejandra.acc_details()