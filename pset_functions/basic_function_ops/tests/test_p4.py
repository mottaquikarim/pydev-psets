"""
Function Basics IV - Multiple Return Values
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p4 import *

@pytest.mark.describe('it returns correct integer sum, product, and quotient of 3 nums')
def test_figures():
	assert figures(21.689,8.123) == (29, 176, 2)

