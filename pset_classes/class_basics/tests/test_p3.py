"""
Rectangle
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p3 import Rectangle


@pytest.mark.describe('it returns corresponding attributes per complete arg input')
class TestRectangle(TestCase):

    def test_init(self):
        r = Rectangle(8, 17)
        assert r.length == 8
        assert r.width == 17

    def test_area(self):
        r = Rectangle(8, 17)
        assert r.area() == 136

    def test_perimeter(self):
        r = Rectangle(8, 17)
        assert r.perimeter() == 50