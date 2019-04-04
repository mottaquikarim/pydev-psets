import io
import pytest
import sys

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Generate Random Phone Number')
class TestPrint(TestCase):

    @pytest.mark.it('Area code supports 718')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p2.random.randint', return_value=1)
    def test_output_718(self, mock_randint, mock_stdout):
        if sys.modules.get('p2'):
            del sys.modules['p2']
        import p2

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert f"1-718-" in stdout_sanitized

    @pytest.mark.it('Area code supports 646')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p2.random.randint', return_value=2)
    def test_output_646(self, mock_randint, mock_stdout):
        if sys.modules.get('p2'):
            del sys.modules['p2']
        import p2

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert f"1-646-" in stdout_sanitized

    @pytest.mark.it('Area code supports 212')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('p2.random.randint', return_value=3)
    def test_output_212(self, mock_randint, mock_stdout):
        if sys.modules.get('p2'):
            del sys.modules['p2']
        import p2

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert f"1-212-" in stdout_sanitized

    @pytest.mark.it('Middle number is between 100 and 999')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_middle(self, mock_stdout):
        if sys.modules.get('p2'):
            del sys.modules['p2']
        import p2

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        middle_num = int(stdout_sanitized.split('-')[2])
        assert middle_num >= 100
        assert middle_num <= 999

    @pytest.mark.it('Middle number is between 1000 and 9999')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_end(self, mock_stdout):
        if sys.modules.get('p2'):
            del sys.modules['p2']
        import p2

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        middle_num = int(stdout_sanitized.split('-')[3])
        assert middle_num >= 1000
        assert middle_num <= 9999
