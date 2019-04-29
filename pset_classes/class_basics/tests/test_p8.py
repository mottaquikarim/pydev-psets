"""
Dogs I - Breeds
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p8 import Dog, Collie, SiberianHusky, Pekingese

# DOG
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestDog(TestCase):

    def test_init(self):
        d = Dog('Rover')
        assert d.name == 'Rover'

    @patch("p8.print")
    def test_bark(self, mock_patch):
        d = Dog('Rover')
        d.bark()
        mock_patch.assert_called_with('Woof!')


# COLLIE
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestCollie(TestCase):

    def test_init(self):
        lassie = Collie('Lassie', 3, 'female')
        assert lassie.name == 'Lassie'
        assert lassie.age == 3
        assert lassie.gender == 'female'
        assert lassie.breed == 'collie'
        assert lassie.temperament == ['devoted', 'graceful', 'athletic', 'intelligent']

    @patch("p8.print")
    def test_bark(self, mock_patch):
        d = Dog('Rover')
        d.bark()
        mock_patch.assert_called_with('Woof!')

    @patch("p8.print")
    def test_herd_the_kids(self, mock_patch):
        lassie = Collie('Lassie', 3, 'female')
        lassie.herd_the_kids()
        mock_patch.assert_called_with('Here are your children!')