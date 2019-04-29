"""
RGB to HEX
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p1 import Color


@pytest.mark.describe('it returns ')
class TestColor(TestCase):

    def test_init(self):
        c = Color('rgb(0, 0, 0)', '#000000')
        assert c.rgb == 'rgb(0, 0, 0)'
        assert c.hex_code == '#000000'

    def test_convert_codes(self):
        c = Color('rgb(0, 0, 0)', '#000000')
        assert c.convert_codes('rgb(0, 0, 0)') == '#000000'
        assert c.convert_codes('#000000') == 'rgb(0, 0, 0)'