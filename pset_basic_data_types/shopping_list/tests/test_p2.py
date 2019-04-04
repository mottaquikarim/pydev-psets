import io
import pytest

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Shopping List Calculator II Tests - Outputs')
class TestPrint(TestCase):

    @pytest.mark.it('Print statements are correctly formatted')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout):
        from p2 import (
            total,
            tax,
            total_total,
        )

        stdout_list = mock_stdout.getvalue().split('\n')
        assert stdout_list[0].strip() == f"TOTAL: ${total}"
        assert stdout_list[1].strip() == f"TAX: ${tax}"
        assert stdout_list[2].strip() == f"TOTAL TOTAL: ${total_total}"


@pytest.mark.describe('Shopping List Calculator II - Variables')
class TestShoppingListItems(TestCase):

    @pytest.mark.it('`total` is the sum of item_prices')
    def test_item_total(self):
        from p1 import (
            item_price_1,
            item_price_2,
            item_price_3,
            item_price_4,
            item_price_5,
        )

        from p2 import total

        assert total == item_price_1 + item_price_2 + \
            item_price_3 + item_price_4 + item_price_5

    @pytest.mark.it('`tax` is `total` * `TAX_RATE`')
    def test_item_tax(self):
        from p2 import (
            total,
            TAX_RATE,
            tax
        )

        assert tax == total * TAX_RATE * 0.01

    @pytest.mark.it('`total_total` is `total` + `tax`')
    def test_item_total_total(self):
        from p2 import (
            total,
            tax,
            total_total,
        )

        assert total_total == total + tax
