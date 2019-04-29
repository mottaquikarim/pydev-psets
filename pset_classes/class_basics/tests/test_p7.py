"""
Vehicles III
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p7 import Vehicle, Car

# VEHICLE
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestVehicle(TestCase):

    def test_init(self):
        v = Vehicle('Yellow Submarine', 'Sgt. Pepper')
        assert v.name == 'Yellow Submarine'
        assert v.owner == 'Sgt. Pepper'
        assert v.category == 'transportation'

    @patch("p7.print")
    def test_start_engine(self, mock_patch):
        v = Vehicle('Yellow Submarine', 'St. Pepper')
        v.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')

# CAR
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestCar(TestCase):

    def test_init(self):
        c = Car('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline', 50, 217)
        assert c.brand == 'Ferrari'
        assert c.plates == 'BD51 SMR'
        assert c.owner == 'Claude Dupont'
        assert c.fuel == 'gasoline'
        assert c.fuel_level == 50
        assert c.max_speed_mph == 217
        assert c.motion == 'drive'
        assert c.terrain == 'land'
        assert c.category == 'transportation'

    @patch("p7.print")
    def test_honk_horn(self, mock_patch):
        c = Car('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline')
        c.honk_horn()
        mock_patch.assert_called_with('HONK!')

    @patch("p7.print")
    def test_check_fuel_level(self, mock_patch):
        c = Car('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline', max_speed_mph = 217)
        c.check_fuel_level()
        mock_patch.assert_called_with('No need to refuel right now.')

    @patch("p7.print")
    def test_check_fuel_level(self, mock_patch):
        c = Car('Tesla', '8CAJ 300', 'Nicole Jackson', 'battery', 12, 155)
        c.check_fuel_level()
        mock_patch.assert_called_with('Refueled 38 units.')

    @patch("p7.print")
    def test_start_engine(self, mock_patch):
        c = Car('Ferrari', 'BD51 SMR', 'Claude Dupont', 'gasoline')
        c.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')