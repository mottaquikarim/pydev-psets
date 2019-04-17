"""
Sum of Squares
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns correct sum given three individual integers')
def test_sum_squares():
	assert sum_squares(4, 5, 6) == 77



@pytest.mark.describe('it returns correct sum given a list')
def test_sum_squares():
	assert sum_squares([2, 6, 3]) == 49



@pytest.mark.describe('it returns correct sum given a tuple')
def test_sum_squares():
	assert sum_squares((3, 6, 9)) == 126



@pytest.mark.describe('it returns correct sum given multiple nested lists')
def test_sum_squares():
	assert sum_squares([4, 5, 6],[8, [6, 3], 2],9) == 271


@pytest.mark.describe('it returns correct sum given a list nested in a tuple')
def test_sum_squares():
	assert sum_squares(4, ([3, 6], 8), 7) == 174