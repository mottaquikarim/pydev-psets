"""
Permutations & Combinations
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


import math
import combinatorics
from sympy.combinatorics import Permutation as p
from sympy.combinatorics import Combination as c


@pytest.mark.describe('it returns 30 for n, r = 6, 2')
def test_perms():
	assert perms(6,2) == p(6,2)



@pytest.mark.describe('it returns 60 for n, r = 6, 2')
def test_combs():
	assert perms(6,2) == p(6,2)