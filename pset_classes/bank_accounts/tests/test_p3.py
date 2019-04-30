"""
Bank Accounts III - Savings Accounts
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p3 import Account, SavingsAccount


@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestAccount(TestCase):

    def test_init(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        assert a.name == 'Alejandra Ochoa'    
        assert a.acc_num == 554951
        assert a.balance == 20000
        assert a.int_rate == 0.5
        assert a.transactions == {}

    @patch("p3.print")
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
class TestSavingsAccount(TestCase):
    def test_init(self):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        assert s.name == 'Priya Ghadiya'    
        assert s.acc_num == 488812
        assert s.balance == 2500
        assert s.int_rate == 2.1
        assert s.transactions == {}

    @patch("p3.print")
    def test_acc_details(self, mock_patch):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        s.acc_details()
        mock_patch.assert_called_with('Account No.: 488812\nAccount Holder: Priya Ghadiya\nInterest Rate: 2.1\nBalance: $2500\n')

    def test_deposit(self):
        s = SavingsAccount('Priya Ghadiya', 488812, 2500)
        s.deposit(1500)
        assert s.balance == 4000
        assert s.transactions == {'Deposit': [2500, 4000]}




