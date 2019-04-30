"""
Bank Accounts VI - Account Activity
"""


import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p6 import Account, SavingsAccount, CheckingAccount


# ACCOUNT
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestAccount(TestCase):

    def test_init(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        assert a.name == 'Alejandra Ochoa'    
        assert a.acc_num == 554951
        assert a.balance == 20000
        assert a.int_rate == 0.5
        assert a.transactions == {}

    @patch("p6.print")
    def test_acc_details(self, mock_patch):
        a = Account('Alejandra Ochoa', 554951, 20000)
        a.acc_details()
        mock_patch.assert_called_with('Account No.: 554951\nAccount Holder: Alejandra Ochoa\nInterest Rate: 0.5\nBalance: $20000\n')

    def test_deposit(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        a.deposit(500)
        assert a.balance == 20500
        assert a.transactions == {'Deposit': [20000, 20500]}

    def test_acc_transfer(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        a.acc_transfer(1750, s)
        assert a.balance == 18250
        assert a.transactions == {'Outgoing Transfer': [20000, 18250]}
        assert s.balance == 4250
        assert s.transactions == {'Deposit': [2500, 4250]}


# SAVINGS ACCOUNT
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestSavingsAccount(TestCase):
    def test_init(self):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        assert s.name == 'Priya Ghadiya'    
        assert s.acc_num == 488812
        assert s.balance == 2500
        assert s.int_rate == 2.1
        assert s.transactions == {}

    @patch("p6.print")
    def test_acc_details(self, mock_patch):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        s.acc_details()
        mock_patch.assert_called_with('Account No.: 488812\nAccount Holder: Priya Ghadiya\nInterest Rate: 2.1\nBalance: $2500\n')

    def test_deposit(self):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        s.deposit(1500)
        assert s.balance == 4000
        assert s.transactions == {'Deposit': [2500, 4000]}

    def test_acc_transfer(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        c.acc_transfer(1750, s)
        assert c.balance == 3250
        assert c.transactions == {'Outgoing Transfer': [5000, 3250]}
        assert s.balance == 4250
        assert s.transactions == {'Deposit': [2500, 4250]}

# CHECKING ACCOUNT
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestCheckingAccount(TestCase):
    def test_init(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        assert c.name == 'Brad Fenwick'    
        assert c.acc_num == 239055
        assert c.balance == 5000
        assert c.int_rate == 1.3
        assert c.transactions == {}

    @patch("p6.print")
    def test_acc_details(self, mock_patch):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        c.acc_details()
        mock_patch.assert_called_with('Account No.: 239055\nAccount Holder: Brad Fenwick\nInterest Rate: 1.3\nBalance: $5000\n')

    def test_deposit(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        c.deposit(1000)
        assert c.balance == 6000
        assert c.transactions == {'Deposit': [5000, 6000]}

    def test_withdraw(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        c.withdraw(1000)
        assert c.balance == 4000
        assert c.transactions == {'Withdrawal': [5000, 4000]}

    def test_acc_transfer(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        c.acc_transfer(1750, s)
        assert c.balance == 3250
        assert c.transactions == {'Outgoing Transfer': [5000, 3250]}
        assert s.balance == 4250
        assert s.transactions == {'Deposit': [2500, 4250]}

    @patch("p6.print")
    def test_acc_activity(self, mock_patch):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        a = Account('Alejandra Ochoa', 554951, 20000)
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)

        a.acc_transfer(1750, s)
        c.deposit(1500)
        c.withdraw(500)
        a.acc_transfer(2250, s)

        c.acc_activity()
        mock_patch.assert_called_with('\nStarting Balance: $6500\nWithdrawal: (-500)\nEnding Balance: $6000')