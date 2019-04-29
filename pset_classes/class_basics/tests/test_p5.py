"""
Vehicles I
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p5 import Vehicle

@pytest.mark.describe('it returns correct instance & class attribute values per arg input')
class TestVehicle(TestCase):

    def test_init(self):
        v = Vehicle('Yellow Submarine', 'Sgt. Pepper')
        assert v.name == 'Yellow Submarine'
        assert v.owner == 'Sgt. Pepper'
        assert v.category == 'transportation'

    @patch("p5.print")
    def test_start_engine(self, mock_patch):
        v = Vehicle('Yellow Submarine', 'Sgt. Pepper')
        v.start_engine()
        mock_patch.assert_called_with('Vrrrrrooomm!')

