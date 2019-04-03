import io
import pytest

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Generate Traffic Light - Outputs')
class TestPrint(TestCase):

    @pytest.mark.it('Prints Red if randnum is 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('pset_conditionals.random_nums.p1.randn', 1)
    def test_output(self, mock_stdout):
        # def r(*args, **kwargs):
        #     return 1
        # mock_randint.return_value = 1
        from pset_conditionals.random_nums.p1 import randn
        f = open('demo.txt', 'a')
        f.write(f"{mock_stdout.getvalue()}")
        f.close()

        assert randn == 1
        assert mock_stdout.getvalue() == 'red'
