"""
Function Basics II - Arguments
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p2 import *

@pytest.mark.describe('it returns ')
def test_names():
	assert names('Taq','Karim') == 'Taq Karim'