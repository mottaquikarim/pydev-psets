import io
import pytest

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Generate Traffic Light - Outputs')
class TestPrint(TestCase):

    @pytest.mark.it('Prints Red if randnum is 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=1)
    def test_output(self, mock_random, mock_stdout):
        import p1

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert p1.randn == 1
        assert stdout_sanitized == 'red'
