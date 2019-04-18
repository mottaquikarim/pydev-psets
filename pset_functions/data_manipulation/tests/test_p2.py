"""
Clean Pairs
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

import math
from p2 import *


@pytest.mark.describe('it returns True if every item in list is a tuple')
def test_cleaner():
	pairs = [('a','b'),('c - d'),('e & f')]
	clean_pairs = cleaner(pairs)

	for i in clean_pairs:
		assert isinstance(i,tuple) == True

@pytest.mark.describe('it returns True if every item in list has length 2')
def test_cleaner():
	pairs = [('a','b'),('c - d'),('e & f')]
	clean_pairs = cleaner(pairs)
	
	for i in clean_pairs:
		assert len(i) == 2