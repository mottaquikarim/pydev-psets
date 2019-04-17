"""
Function Basics V - Indeterminate Arguments
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns highest and lowest value of ')
def test_high_low(*nums):
	assert high_low(15, [21, 3], 6, 11) == 
	assert high_low(15, 4, 8, 21, 11) == 