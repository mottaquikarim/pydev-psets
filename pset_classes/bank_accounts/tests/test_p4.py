"""
Bank Accounts IV - Checking Accounts
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p4 import Account, CheckingAccount


@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestAccount(TestCase):

    def test_init(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        assert a.name == 'Alejandra Ochoa'    
        assert a.acc_num == 554951
        assert a.balance == 20000
        assert a.int_rate == 0.5
        assert a.transactions == {}

    @patch("p4.print")
    def test_acc_details(self, mock_patch):
        a = Account('Alejandra Ochoa', 554951, 20000)
        a.acc_details()
        mock_patch.assert_called_with('Account No.: 554951\nAccount Holder: Alejandra Ochoa\nInterest Rate: 0.5\nBalance: $20000\n')

    def test_deposit(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        a.deposit(500)
        assert a.balance == 20500
        assert a.transactions == {'Deposit': [20000, 20500]}


@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestCheckingAccount(TestCase):
    def test_init(self):
        c = CheckingAccount('Brad Fenwick', 239055, 5000)
        assert c.name == 'Brad Fenwick'    
        assert c.acc_num == 239055
        assert c.balance == 5000
        assert c.int_rate == 1.3
        assert c.transactions == {}

    @patch("p4.print")
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




