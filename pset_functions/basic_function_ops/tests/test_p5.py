"""
Function Basics V - Indeterminate Arguments
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p5 import *

@pytest.mark.describe('it returns highest and lowest value of input numbers')
def test_high_low():
	assert high_low(15, 4, 8, 21, 11) == (21, 4)


@pytest.mark.describe('it returns an error if argument pass is not int type')
def test_high_low():
	assert high_low(15, [21, 3], 6, 11) == ('Error: ', 'Please enter only individual integers.')