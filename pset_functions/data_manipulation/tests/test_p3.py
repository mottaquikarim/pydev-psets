"""
Password Requirements
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p3 import *


@pytest.mark.describe('it returns error if length < 6')
def test_pw_validator():
	pw = 'abc'
	assert pw_validator('abc') == 'Please enter a valid password.'


@pytest.mark.describe('it returns error if length > 16')
def test_pw_validator():
	pw = '1234567890abcdefg'
	assert pw_validator('1234567890abcdefg') == 'Please enter a valid password.'


@pytest.mark.describe('it returns error if pw has no numbers')
def test_pw_validator():
	pw = '@bcdEFGh!j'
	assert pw_validator('@bcdEFGh!j') == 'Please enter a valid password.'


@pytest.mark.describe('it returns error if pw has no lowercase letters')
def test_pw_validator():
	pw = '@BCD3EFGH!J'
	assert pw_validator('@BCD3EFGH!J') == 'Please enter a valid password.'


@pytest.mark.describe('it returns error if pw has no uppercase letters')
def test_pw_validator():
	pw = '@bcd3efgh!j'
	assert pw_validator('@bcd3efgh!j') == 'Please enter a valid password.'


@pytest.mark.describe('it returns error if pw has no special characters')
def test_pw_validator():
	pw = 'Abcd3FGhIj112'
	assert pw_validator('Abcd3FGhIj112') == 'Please enter a valid password.'


@pytest.mark.describe('it returns success if pw is valid per requirements')
def test_pw_validator():
	pw = 'P$kj35S&7'
	assert pw_validator('P$kj35S&7') == 'Success!'