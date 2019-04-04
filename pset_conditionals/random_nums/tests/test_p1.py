import io
import pytest
import sys

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Generate Traffic Light')
class TestPrint(TestCase):

    @pytest.mark.it('Prints Red if randnum is 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p1.random.randint', return_value=1)
    def test_output_red(self, mock_randint, mock_stdout):
        del sys.modules['p1']
        import p1
        # print(p1.randn)
        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert stdout_sanitized == 'red'

    @pytest.mark.it('Prints Green if randnum is 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p1.random.randint', return_value=2)
    def test_output_green(self, mock_randint, mock_stdout):
        del sys.modules['p1']
        import p1
        # print(p1.randn)
        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert stdout_sanitized == 'green'

    @pytest.mark.it('Prints Yellow if randnum is 3')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p1.random.randint', return_value=3)
    def test_output_yellow(self, mock_randint, mock_stdout):
        del sys.modules['p1']
        import p1
        # print(p1.randn)
        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert stdout_sanitized == 'yellow'
