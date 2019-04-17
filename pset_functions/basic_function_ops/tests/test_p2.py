"""
Function Basics II - Arguments
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns ')
def test_names(first,last):
	assert names('Taq','Karim') == 'Taq Karim'