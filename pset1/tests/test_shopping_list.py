import unittest

from pset1.shopping_list import item_name_1, item_price_1, item_quant_1


class TestList(unittest.TestCase):
    def test_shopping_list(self):
        """
        Test that it can sum a list of integers
        """
        assert item_name_1 == 'test'
