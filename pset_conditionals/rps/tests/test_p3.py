import io
import pytest
import sys

from unittest import TestCase
from unittest.mock import patch


@pytest.mark.describe('Play RPS w/Input')
class TestPrint(TestCase):
    vals = ["1", "3"]

    def set_pvals(self):
        vals = self.vals

        def ret(*args, **kwargs):
            nonlocal vals
            r = vals[0]
            vals = vals[1:]
            return r

        return ret

    @pytest.mark.it('if p1 and p2 are equal then print 0')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_tie(self, mock_input, mock_stdout):
        mock_input.return_value = '1'
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "0" in stdout_sanitized

    @pytest.mark.it('if p1 is r and p2 is s, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_rs(self, mock_input, mock_stdout):
        self.vals = ["r", "s"]
        mock_input.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is r and p2 is p, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_rp(self, mock_input, mock_stdout):
        self.vals = ["r", "p"]
        mock_input.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized

    @pytest.mark.it('if p1 is s and p2 is p, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_sp(self, mock_randint, mock_stdout):
        self.vals = ["s", "p"]
        mock_randint.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is s and p2 is r, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_sr(self, mock_randint, mock_stdout):
        self.vals = ["s", "r"]
        mock_randint.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized

    @pytest.mark.it('if p1 is p and p2 is r, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_pr(self, mock_randint, mock_stdout):
        self.vals = ["p", "r"]
        mock_randint.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is p and p2 is s, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input')
    def test_output_ps(self, mock_randint, mock_stdout):
        self.vals = ["p", "s"]
        mock_randint.side_effect = self.set_pvals()
        if sys.modules.get('p3'):
            del sys.modules['p3']
        import p3

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized
