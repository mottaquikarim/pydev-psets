"""
Bank Accounts I - Opening An Account
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p1 import Account


@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestAccount(TestCase):

    def test_init(self):
        a = Account('Alejandra Ochoa', 554951, 20000)
        assert a.name == 'Alejandra Ochoa'    
        assert a.acc_num == 554951
        assert a.balance == 20000
        assert a.int_rate == 0.5

    @patch("p1.print")
    def test_acc_details(self, mock_patch):
        a = Account('Alejandra Ochoa', 554951, 20000)
        a.acc_details()
        mock_patch.assert_called_with('Account No.: 554951\nAccount Holder: Alejandra Ochoa\nInterest Rate: 0.5\nBalance: $20000\n')

