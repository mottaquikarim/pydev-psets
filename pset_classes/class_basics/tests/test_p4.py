"""
Circle
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p4 import Circle


@pytest.mark.describe('it returns correct instance & class attribute values per arg input')
class TestCircle(TestCase):

    def test_init(self):
        c = Circle(7)
        assert c.radius == 7
        assert c.pi == 3.14159

    def test_area(self):
        c = Circle(7)
        assert c.area() == 153.93791

    def test_perimeter(self):
        c = Circle(7)
        assert c.perimeter() == 43.98226

