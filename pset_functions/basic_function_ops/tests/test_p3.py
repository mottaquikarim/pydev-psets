"""
Function Basics III - Default Arguments
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns ')
def test_fave_colors(first,last,color=None):

	
	assert fave_colors() == 