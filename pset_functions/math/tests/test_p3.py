"""
Multiples
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns 0 if both num1 and num2 each > limit')
def test_sum_multiples():
	assert sum_multiples(9,21,6) == 0



@pytest.mark.describe('it returns the sum of either num1 or num2 if the other > limit')
def test_sum_multiples():
	assert sum_multiples(3,17,12) == 30
	assert sum_multiples(17,3,12) == 30


@pytest.mark.describe('it returns the sum of either num1 or num2 if the other > limit')
def test_sum_multiples():
	assert sum_multiples(4,9,21) == 87