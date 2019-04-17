"""
Rainbows & Wobniars
"""

# import io
# import pytest
# from unittest import TestCase
# from unittest.mock import patch


@pytest.mark.describe('it returns a list with red, yellow, blue, & violet spelled backwards')
def test_wobniar():
	assert wobniar() == ['der', 'wolley', 'eulb', 'teloiv']