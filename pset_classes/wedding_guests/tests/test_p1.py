"""
Weddings I - Guest List
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p1 import Guest, Bridesmaid


# GUEST
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestGuest(TestCase):

    def test_init(self):
        g = Guest('Michelle Addison', 9205150102)
        assert g.name == 'Michelle Addison'    
        assert g.phone == 9205150102
        assert g.invite_sent == False


    def test_send_invite(self):
        g = Guest('Michelle Addison', 9205150102)
        g.send_invite()
        assert g.invite_sent == True


# BRIDESMAID
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestBridesmaid(TestCase):

    def test_init(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        assert b.name == 'Angelika Vasilieva'    
        assert b.phone == 2019352087
        assert b.invite_sent == False


    def test_send_invite(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        b.send_invite()
        assert b.invite_sent == True


# CHECK CLASS FUNCTION

@pytest.mark.describe('it returns True if pass instance of Bridesmaid and Bridesmaid class')
def check_class():
    b = Bridesmaid('Angelika Vasilieva', 2019352087)
    assert check_class(b, Bridesmaid) == True

@pytest.mark.describe('it returns True if pass instance of Guest and Guest class')
def check_class():
    g = Guest('Michelle Addison', 9205150102)
    assert check_class(g, Guest) == True

@pytest.mark.describe('it returns True if pass instance of Bridesmaid and Guest class')
def check_class():
    b = Bridesmaid('Angelika Vasilieva', 2019352087)
    assert check_class(b, Guest) == True

@pytest.mark.describe('it returns False if pass instance of Guest and Bridesmaid class')
def check_class():
    g = Guest('Michelle Addison', 9205150102)
    assert check_class(g, Bridesmaid) == False
