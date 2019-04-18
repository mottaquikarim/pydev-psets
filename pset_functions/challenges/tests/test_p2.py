"""
Speeding Tickets
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
import math
from p1 import *


@pytest.mark.describe('it passes if speed < 70 and it returns 0 new points')
def test_speed_checker():
	plate = 'ABC123'
	speed = 70

	test_return = speed_checker(plate, speed)
	plate, new_points = test_return

	assert new_points == 0


@pytest.mark.describe('it passes if speed == 70 and it returns 0 new points')
def test_speed_checker():
	plate = 'ABC123'
	speed = 70

	test_return = speed_checker(plate, speed)
	plate, new_points = test_return

	assert new_points == 0


@pytest.mark.describe('it passes if speed (???> 70???) and it returns ...')
def test_speed_checker():
	plate = 'ABC123'
	speed = 71 #how test every num in an interval...?

	test_return = speed_checker(plate, speed)
	plate, new_points = test_return

	if 71 <= speed <= 75:
		assert new_points == 1

	# plate = 'ABC123'
	# speed = 71

	# test_return = speed_checker(plate, speed)
	# plate, new_points = test_return

	# assert new_points == 1


@pytest.mark.describe('it passes if license points >= BEFORE adding new_points')
def test_speeders():


	assert result == f'{plate}: Violating license suspension! CAR CHASE!!!'




@pytest.mark.describe('it passes if license points < 12 and driver gets 0 new_points')
def test_speeders():

	assert result == f'{plate}: Good'





@pytest.mark.describe('it passes if license points < 12 AFTER adding new_points')
def test_speeders():


	assert result == f'{plate}: Points added. Catch the speeder!'




@pytest.mark.describe('it passes if license points >= 12 AFTER adding new_points')
def test_speeders():


	assert result == f'{plate}: Points added and license suspended. CAR CHASE!!!'


