"""
Simple Interest Calculator
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

import math
from p1 import *


@pytest.mark.describe('it returns correct value for the interest accrued')
def test_simple_interest():
	p = 1500
	r = 2.4
	t = 60

	a, b = simple_interest(p,r,t)
	assert a == 15.62

@pytest.mark.describe('it returns correct value for the interest accrued')
def test_simple_interest():
	p = 1500
	r = 2.4
	t = 60

	a, b = simple_interest(p,r,t)
	assert b == 1515.62




