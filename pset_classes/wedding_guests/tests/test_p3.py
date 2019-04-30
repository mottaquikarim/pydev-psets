"""
Weddings III - Record Shower & Bachelorette RSVP
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p3 import Guest, Bridesmaid


# GUEST 1
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestGuest(TestCase):

    def test_init(self):
        g = Guest('Michelle Addison', 9205150102)
        assert g.name == 'Michelle Addison'    
        assert g.phone == 9205150102
        assert g.invite_sent == False
        assert g.diet == None
        assert g.rsvp == None
        assert g.plus_one == None
        assert g.plus_one_name == None
        assert g.plus_one_diet == None

    def test_send_invite(self):
        g = Guest('Michelle Addison', 9205150102)
        g.send_invite()
        assert g.invite_sent == True

    def test_record_rsvp(self):
        g = Guest('Klauss Wagner', 3748807716)
        g.record_rsvp('yes', 'Vegetarian', 'Yes', 'Vincent Ahmad', 'Halal')
        assert g.rsvp == True
        assert g.diet == 'Vegetarian'
        assert g.plus_one == True
        assert g.plus_one_name == 'Vincent Ahmad'
        assert g.plus_one_diet == 'Halal'


# GUEST 2
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestGuest(TestCase):

    def test_init(self):
        g = Guest('Michelle Addison', 9205150102, True)
        assert g.name == 'Michelle Addison'    
        assert g.phone == 9205150102
        assert g.invite_sent == True
        assert g.diet == None
        assert g.rsvp == None
        assert g.plus_one == None
        assert g.plus_one_name == None
        assert g.plus_one_diet == None

    def test_record_rsvp(self):
        g = Guest('Michelle Addison', 9205150102, True)
        g.record_rsvp('Yes', None, 'No')
        assert g.rsvp == True
        assert g.diet == None
        assert g.plus_one == False
        assert g.plus_one_name == None
        assert g.plus_one_diet == None

# BRIDESMAID
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestBridesmaid(TestCase):

    def test_init(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        assert b.name == 'Angelika Vasilieva'    
        assert b.phone == 2019352087
        assert b.invite_sent == False
        assert b.diet == None
        assert b.rsvp == None
        assert b.plus_one == None
        assert b.plus_one_name == None
        assert b.plus_one_diet == None
        assert b.shower_rsvp == None
        assert b.bachelorette_rsvp == None


    def test_send_invite(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        b.send_invite()
        assert b.invite_sent == True


    def test_record_rsvp(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        b.record_rsvp('Yes', 'Kosher', 'yes', 'Claude Dupont', None)
        assert b.rsvp == True
        assert b.diet == 'Kosher'
        assert b.plus_one == True
        assert b.plus_one_name == 'Claude Dupont'
        assert b.plus_one_diet == None


    def test_record_shower_rsvp(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        b.record_shower_rsvp('no')
        assert b.shower_rsvp == False

    def test_record_bachelorette_rsvp(self):
        b = Bridesmaid('Angelika Vasilieva', 2019352087)
        b.record_bachelorette_rsvp('Yes')
        assert b.bachelorette_rsvp == True

