"""
Phone Contacts
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p2 import Contact


@pytest.mark.describe('it returns corresponding attributes per complete arg input')
class TestContact(TestCase):

    def test_init(self):
        x = Contact('Alejandra', 'Ochoa', 19034882739, 17243756608, 'alejandra.ochoa@gmail.com')
        assert x.first_name == 'Alejandra'
        assert x.last_name == 'Ochoa'
        assert x.mobile_num == 19034882739
        assert x.work_num == 17243756608
        assert x.email == 'alejandra.ochoa@gmail.com'

@pytest.mark.describe('it returns corresponding attributes per incomplete arg input')
class TestContact(TestCase):

    def test_init(self):
        y = Contact('Brad', 'Fenworth', 12284001753, email = 'brad.fenworth@gmail.com')
        assert y.first_name == 'Brad'
        assert y.last_name == 'Fenworth'
        assert y.mobile_num == 12284001753
        assert y.work_num == None
        assert y.email == 'brad.fenworth@gmail.com'