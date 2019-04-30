"""
Bank Accounts VI - Account Activity
"""

# Create a method called "acc_activity" within the Account class. For each transaction made in an account, this method should print out the account number, the starting balance, the type of transaction, the value of the transaction, and the ending balance. It should look something like this:

"""
Account: 554951
Starting Balance: $20000
Outgoing Transfer: (-1750) --> or Deposit: +1500
Ending Balance: $18250
"""

# Call this method on each type of account after completing at least one transaction for each.


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

    def acc_activity(self):
        print(f'\nAccount: {self.acc_num}')
        count = 0
        for k, v in self.transactions.items():
            diff = v[1] - v[0]
            if k == 'Withdrawal':
                print(f'''
Starting Balance: ${v[0]}
Withdrawal: ({diff})
Ending Balance: ${v[1]}''')
            elif k == 'Outgoing Transfer':
                print(f'''
Starting Balance: ${v[0]}
Outgoing Transfer: ({diff})
Ending Balance: ${v[1]}''')
            elif k == 'Deposit':
                print(f'''
Starting Balance: ${v[0]}
Deposit: +{diff}
Ending Balance: ${v[1]}''')
            count += 1

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



alejandra = Account('Alejandra Ochoa', 554951, 20000)
priya = SavingsAccount('Priya Ghadiya', 488812, 2500)
brad = CheckingAccount('Brad Fenwick', 239055, 5000)

alejandra.deposit(175)
alejandra.acc_transfer(1750, priya)
priya.deposit(1500)
brad.acc_transfer(250, priya)
brad.withdraw(250)


alejandra.acc_activity()
priya.acc_activity()
brad.acc_activity()