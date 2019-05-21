import io
import pytest

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Shopping List Calculator II - Outputs')
class TestPrint(TestCase):

    @pytest.mark.it('Print statements are correctly formatted')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout):
        from p3 import (
            item_name_1,
            item_name_2,
            item_name_3,
            item_name_4,
            item_name_5,
            item_price_1,
            item_price_2,
            item_price_3,
            item_price_4,
            item_price_5,
            item_quant_1,
            item_quant_2,
            item_quant_3,
            item_quant_4,
            item_quant_5,
        )

        stdout_list = mock_stdout.getvalue().split('\n')

        assert stdout_list[0].strip() == f"{item_quant_1} {item_name_1} = ${item_quant_1*item_price_1}"
        assert stdout_list[1].strip() == f"{item_quant_2} {item_name_2} = ${item_quant_2*item_price_2}"
        assert stdout_list[2].strip() == f"{item_quant_3} {item_name_3} = ${item_quant_3*item_price_3}"
        assert stdout_list[3].strip() == f"{item_quant_4} {item_name_4} = ${item_quant_4*item_price_4}"
        assert stdout_list[4].strip() == f"{item_quant_5} {item_name_5} = ${item_quant_5*item_price_5}"


@pytest.mark.describe('Shopping List Calculator III - Inputs')
class TestInputsCalled(TestCase):

    @pytest.mark.it('Input is called 15 times')
    @patch('p3.input')
    def test_input_called(self, mockInput):
        assert mockInput.call_count == 15


@pytest.mark.describe('Shopping List Calculator III - Variables')
class TestShoppingListItems(TestCase):

    @pytest.mark.it('Item names are strings')
    def test_item_names(self):
        from p3 import (
            item_name_1,
            item_name_2,
            item_name_3,
            item_name_4,
            item_name_5,
        )

        assert isinstance(item_name_1, str)
        assert isinstance(item_name_2, str)
        assert isinstance(item_name_3, str)
        assert isinstance(item_name_4, str)
        assert isinstance(item_name_5, str)

    @pytest.mark.it('Item prices are floats')
    def test_item_prices(self):
        from p3 import (
            item_price_1,
            item_price_2,
            item_price_3,
            item_price_4,
            item_price_5,
        )

        assert isinstance(item_price_1, float)
        assert isinstance(item_price_2, float)
        assert isinstance(item_price_3, float)
        assert isinstance(item_price_4, float)
        assert isinstance(item_price_5, float)

    @pytest.mark.it('Item quants are ints')
    def test_item_quants(self):
        from p3 import (
            item_quant_1,
            item_quant_2,
            item_quant_3,
            item_quant_4,
            item_quant_5,
        )

        assert isinstance(item_quant_1, int)
        assert isinstance(item_quant_2, int)
        assert isinstance(item_quant_3, int)
        assert isinstance(item_quant_4, int)
        assert isinstance(item_quant_5, int)
