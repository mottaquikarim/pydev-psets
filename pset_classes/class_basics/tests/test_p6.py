"""
Vehicles II
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p6 import Vehicle, Car, Plane, Boat

# VEHICLE
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestVehicle(TestCase):

    def test_init(self):
        v = Vehicle('Yellow Submarine', 'Sgt. Pepper')
        assert v.name == 'Yellow Submarine'
        assert v.owner == 'Sgt. Pepper'
        assert v.category == 'transportation'

    @patch("p6.print")
    def test_start_engine(self, mock_patch):
        v = Vehicle('Yellow Submarine', 'St. Pepper')
        v.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')

# CAR
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestCar(TestCase):

    def test_init(self):
        c = Car('The Batmobile','Batman')
        assert c.name == 'The Batmobile'
        assert c.owner == 'Batman'
        assert c.motion == 'drive'
        assert c.terrain == 'land'
        assert c.category == 'transportation'

    @patch("p6.print")
    def test_honk_horn(self, mock_patch):
        c = Car('The Batmobile','Batman')
        c.honk_horn()
        mock_patch.assert_called_with('HONK!')

    @patch("p6.print")
    def test_start_engine(self, mock_patch):
        c = Car('The Batmobile','Batman')
        c.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')

# PLANE
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestPlane(TestCase):

    def test_init(self):
        p = Plane('The Canary', 'Amelia Earhart')
        assert p.name == 'The Canary'
        assert p.owner == 'Amelia Earhart'
        assert p.motion == 'fly'
        assert p.terrain == 'air'
        assert p.category == 'transportation'

    @patch("p6.print")
    def test_take_off(self, mock_patch):
        p = Plane('The Canary', 'Amelia Earhart')
        p.take_off()
        mock_patch.assert_called_with('Fasten your seatbelts!')

    @patch("p6.print")
    def test_start_engine(self, mock_patch):
        p = Plane('The Canary', 'Amelia Earhart')
        p.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')

# BOAT
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestBoat(TestCase):

    def test_init(self):
        b = Boat('Jenny', 'Forrest Gump')
        assert b.name == 'Jenny'
        assert b.owner == 'Forrest Gump'
        assert b.motion == 'sail'
        assert b.terrain == 'water'
        assert b.category == 'transportation'

    @patch("p6.print")
    def test_drop_anchor(self, mock_patch):
        b = Boat('Jenny', 'Forrest Gump')
        b.drop_anchor()
        mock_patch.assert_called_with('Anchors away!')

    @patch("p6.print")
    def test_start_engine(self, mock_patch):
        b = Boat('Jenny', 'Forrest Gump')
        b.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')
