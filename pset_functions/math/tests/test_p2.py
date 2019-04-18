"""
Permutations & Combinations
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch


import math
from p2 import *

@pytest.mark.describe('it returns 30 for n, r = 6, 2')
def test_perms():
	assert perms(6,2) == 30

@pytest.mark.describe('it returns 60 for n, r = 6, 2')
def test_combs():
	assert combs(6,2) == 60

