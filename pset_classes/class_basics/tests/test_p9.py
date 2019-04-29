"""
Dogs II - Tricks
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p9 import Dog, Collie, SiberianHusky, Pekingese


# DOG
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestDog(TestCase):

    def test_init(self):
        d = Dog('Rover')
        assert d.name == 'Rover'    
        assert d.tricks == {'shake_hands': False, 'fetch': False, 'spin': False, 'roll_over': False}

    @patch("p9.print")
    def test_bark(self, mock_patch):
        d = Dog('Rover')
        d.bark()
        mock_patch.assert_called_with('Woof!')

    
    # def test_learn_trick(self, trick):
    #     pass


# COLLIE INIT & MAIN METHODS
@pytest.mark.describe('it returns correct instance & class attribute values per arg input')
class TestCollie(TestCase):

    def test_init(self):
        lassie = Collie('Lassie', 3, 'female', fetch = True, spin = True)
        assert lassie.name == 'Lassie'
        assert lassie.age == 3
        assert lassie.gender == 'female'
        assert lassie.breed == 'collie'
        assert lassie.temperament == ['devoted', 'graceful', 'athletic', 'intelligent']
        assert lassie.tricks == {'shake_hands': False, 'fetch': True, 'spin': True, 'roll_over': False }

    @patch("p9.print")
    def test_bark(self, mock_patch):
        d = Dog('Rover')
        d.bark()
        mock_patch.assert_called_with('Woof!')

    @patch("p9.print")
    def test_herd_the_kids(self, mock_patch):
        lassie = Collie('Lassie', 3, 'female')
        lassie.herd_the_kids()
        mock_patch.assert_called_with('Here are your children!')

    def test_learn_trick(self):
        lassie = Collie('Lassie', 3, 'female')
        lassie.learn_trick('shake_hands')
        assert lassie.tricks['shake_hands'] == True

# PEKINGESE TRICKS FALSE
@pytest.mark.describe('it returns correct method output when tricks are False')
class TestPekingese(TestCase):


    # shake_hands False
    @patch("p9.print")
    def test_shake_hands(self, mock_patch):
        cameron = Pekingese('Cameron', 8, 'female', roll_over = True)
        cameron.shake_hands()
        mock_patch.assert_called_with('Shake hands? I don\'t know that trick.')

    # fetch False
    @patch("p9.print")
    def test_fetch(self, mock_patch):
        cameron = Pekingese('Cameron', 8, 'female', spin = True)
        cameron.fetch()
        mock_patch.assert_called_with('Fetch? I don\'t know that trick.')

    # spin False
    @patch("p9.print")
    def test_spin(self, mock_patch):
        cameron = Pekingese('Cameron', 8, 'female', True)
        cameron.spin()
        mock_patch.assert_called_with('Spin? I don\'t know that trick.')

    # roll_over False
    @patch("p9.print")
    def test_roll_over(self, mock_patch):
        cameron = Pekingese('Cameron', 8, 'female', True, True)
        cameron.roll_over()
        mock_patch.assert_called_with('Roll over? I don\'t know that trick.')


# HUSKY TRICKS TRUE
@pytest.mark.describe('it returns correct method output when tricks are True')
class TestSiberianHusky(TestCase):

    @patch("p9.print")
    def test_pull_sled(self, mock_patch):
        aiden = SiberianHusky('Aiden', 5, 'male', True, True, roll_over = True)
        aiden.pull_sled()
        mock_patch.assert_called_with('I\'m mushing already!')

    # shake_hands True
    @patch("p9.print")
    def test_shake_hands(self, mock_patch):
        aiden = SiberianHusky('Aiden', 5, 'male', True, True, roll_over = True)
        aiden.shake_hands()
        mock_patch.assert_called_with('Shake hands? Done - treat please!')

    # fetch True
    @patch("p9.print")
    def test_fetch(self, mock_patch):
        aiden = SiberianHusky('Aiden', 5, 'male', True, True, roll_over = True)
        aiden.fetch()
        mock_patch.assert_called_with('Fetch? Done - treat please!')

    # spin True
    @patch("p9.print")
    def test_spin(self, mock_patch):
        aiden = SiberianHusky('Aiden', 5, 'male', True, spin = True, roll_over = True)
        aiden.spin()
        mock_patch.assert_called_with('Spin? Done - treat please!')

    # roll_over True
    @patch("p9.print")
    def test_roll_over(self, mock_patch):
        aiden = SiberianHusky('Aiden', 5, 'male', roll_over = True)
        aiden.roll_over()
        mock_patch.assert_called_with('Roll over? Done - treat please!')

