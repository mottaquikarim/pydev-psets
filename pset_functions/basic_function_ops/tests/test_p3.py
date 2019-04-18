"""
Function Basics III - Default Arguments
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p3 import *

@pytest.mark.describe('it returns <full name>: <favorite color> as a dict if all args entered')
def test_fave_colors():
	assert fave_colors('Taq','Karim','blue') == {'Taq Karim': 'blue'}

@pytest.mark.describe('it returns <full name>: None (the default value) as a dict if only first & last name entered')
def test_fave_colors():
	assert fave_colors('Ricardo','Galbis') == {'Ricardo Galbis': None}