import ast
import inspect
import io
import pytest
import sys

from unittest import TestCase
from unittest.mock import patch

import p1


def update_tree(tree, var_name, var_val):
        # https://python-ast-explorer.com/
        # https://greentreesnakes.readthedocs.io/en/latest/index.html
    for node in ast.walk(tree):
        is_assigning = isinstance(node, ast.Assign)
        if not is_assigning:
            continue

        targets = node.targets
        var_names = [1 for t in targets if t.id == var_name]

        if not len(var_names):
            continue

        node.value = ast.parse(f"{var_val.__repr__()}").body[0].value

    return tree


def compile_and_exec(module, updates=None):
    if not updates:
        updates = []

    str_ = inspect.getsource(module)
    tree = ast.parse(str_)
    for update in updates:
        var_name, var_val = update
        tree = update_tree(tree, var_name, var_val)

    exec(compile(tree, filename="<ast>", mode="exec"))


@pytest.mark.describe('Play RPS')
class TestPrint(TestCase):
    @pytest.mark.it('if p1 and p2 are equal then print 0')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_tie(self, mock_stdout):
        compile_and_exec(p1, [("p1", "p"), ("p2", "p")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "0" in stdout_sanitized

    @pytest.mark.it('if p1 is r and p2 is s, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_rs(self, mock_stdout):
        compile_and_exec(p1, [("p1", "r"), ("p2", "s")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is r and p2 is p, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_rp(self, mock_stdout):
        compile_and_exec(p1, [("p1", "r"), ("p2", "p")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized

    @pytest.mark.it('if p1 is s and p2 is p, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_sp(self, mock_stdout):
        compile_and_exec(p1, [("p1", "s"), ("p2", "p")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is s and p2 is r, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_sr(self, mock_stdout):
        compile_and_exec(p1, [("p1", "s"), ("p2", "r")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized

    @pytest.mark.it('if p1 is p and p2 is r, print 1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_pr(self, mock_stdout):
        compile_and_exec(p1, [("p1", "p"), ("p2", "r")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "1" in stdout_sanitized

    @pytest.mark.it('if p1 is p and p2 is s, print 2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_ps(self, mock_stdout):
        compile_and_exec(p1, [("p1", "p"), ("p2", "s")])

        stdout_sanitized = mock_stdout.getvalue().replace('\n', '')
        assert "2" in stdout_sanitized
