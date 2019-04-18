"""
RGB to Hex
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p2 import *

@pytest.mark.describe('it returns error msg if color not in database')
def test_rgb_hex():
	color1 = (5, 91, 0)
	assert rgb_hex(color1) == 'Sorry we don\'t have that color on file. Please make sure you entered the color with its correct syntax.'
	color2 = '2f2f3f'
	assert rgb_hex(color2) == 'Sorry we don\'t have that color on file. Please make sure you entered the color with its correct syntax.'

@pytest.mark.describe('it returns correct hex value if full rgb string passed')
def test_rgb_hex():
	color = 'rgb(89, 5, 198)'
	assert rgb_hex(color) == '#5905c6'

@pytest.mark.describe('it returns correct rgb value if full hex string passed')
def test_rgb_hex():
	color = '#b7ffb8'
	assert rgb_hex(color) == 'rgb(183, 255, 184)'

@pytest.mark.describe('it returns correct hex value if rgb passed as tuple')
def test_rgb_hex():
	color = (255, 191, 0)
	assert rgb_hex(color) == '#ffbf00'

@pytest.mark.describe('it returns correct rgb value if hex passed without # char')
def test_rgb_hex():
	color = 'ff5e6e'
	assert rgb_hex(color) == 'rgb(255, 94, 110)'

