"""
GPA Calculator
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p1 import *

@pytest.mark.describe('asserts True if conversion is correct')
def test_simple_gpa():
	gpa = simple_gpa('A+')
	assert gpa == 4.0
	gpa = simple_gpa('A')
	assert gpa == 4.0
	gpa = simple_gpa('A-')
	assert gpa == 3.7
	gpa = simple_gpa('B+')
	assert gpa == 3.3
	gpa = simple_gpa('B')
	assert gpa == 3.0
	gpa = simple_gpa('B-')
	assert gpa == 2.7
	gpa = simple_gpa('C+')
	assert gpa == 2.3
	gpa = simple_gpa('C')
	assert gpa == 2.0
	gpa = simple_gpa('C-')
	assert gpa == 1.7
	gpa = simple_gpa('D+')
	assert gpa == 1.3
	gpa = simple_gpa('D')
	assert gpa == 1.0
	gpa = simple_gpa('D-')
	assert gpa == 0.7
	gpa = simple_gpa('F')
	assert gpa == 0.0


