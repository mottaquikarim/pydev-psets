"""
Fromagerie III - Cheeses
"""


import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p3 import ProductCat, Cheese


# PRODUCT CATEGORY
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestProductCat(TestCase):
    def test_init(self):
        cheese_inventory = {'brie': ['DRY8900', 27, 11, 5], 'feta': ['DRY7730', 74, 13, 9], 'cheddar': ['DRY3673', 2, 15, 1], 'mozzarella': ['DRY7506', 17, 13, 3], 'ricotta': ['DRY9723', 60, 14, 3], 'provolone': ['DRY5895', 55, 14, 7], 'gruyere': ['DRY3934', 49, 11, 4], 'pecorino romano': ['DRY9980', 24, 10, 8], 'parmigiano reggiano': ['DRY1601', 79, 10, 0], 'gorgonzola': ['DRY6408', 72, 18, 8], 'pepper jack': ['DRY2506', 85, 10, 9], 'gouda': ['DRY4270', 83, 15, 9], 'asiago': ['DRY1592', 42, 18, 2], 'mascarpone': ['DRY6230', 62, 17, 9], 'cotija': ['DRY4128', 95, 16, 5], 'manchego': ['DRY8027', 47, 11, 3]}
        cheeses = ProductCat('cheese', cheese_inventory)
        assert cheeses.name == 'cheese'    
        assert cheeses.inventory == {'brie': ['DRY8900', 27, 11, 5], 'feta': ['DRY7730', 74, 13, 9], 'cheddar': ['DRY3673', 2, 15, 1], 'mozzarella': ['DRY7506', 17, 13, 3], 'ricotta': ['DRY9723', 60, 14, 3], 'provolone': ['DRY5895', 55, 14, 7], 'gruyere': ['DRY3934', 49, 11, 4], 'pecorino romano': ['DRY9980', 24, 10, 8], 'parmigiano reggiano': ['DRY1601', 79, 10, 0], 'gorgonzola': ['DRY6408', 72, 18, 8], 'pepper jack': ['DRY2506', 85, 10, 9], 'gouda': ['DRY4270', 83, 15, 9], 'asiago': ['DRY1592', 42, 18, 2], 'mascarpone': ['DRY6230', 62, 17, 9], 'cotija': ['DRY4128', 95, 16, 5], 'manchego': ['DRY8027', 47, 11, 3]}
        assert cheeses.food_group == 'dairy'
        assert cheeses.production_standards == ['organic', 'non-GMO', 'carbon neutral']
        assert cheeses.source == 'Cheesequake Farms'

    @patch("p3.print")
    def test_view_inventory(self, mock_patch):
        cheese_inventory = {'brie': ['DRY8900', 27, 11, 5], 'feta': ['DRY7730', 74, 13, 9], 'cheddar': ['DRY3673', 2, 15, 1], 'mozzarella': ['DRY7506', 17, 13, 3], 'ricotta': ['DRY9723', 60, 14, 3], 'provolone': ['DRY5895', 55, 14, 7], 'gruyere': ['DRY3934', 49, 11, 4], 'pecorino romano': ['DRY9980', 24, 10, 8], 'parmigiano reggiano': ['DRY1601', 79, 10, 0], 'gorgonzola': ['DRY6408', 72, 18, 8], 'pepper jack': ['DRY2506', 85, 10, 9], 'gouda': ['DRY4270', 83, 15, 9], 'asiago': ['DRY1592', 42, 18, 2], 'mascarpone': ['DRY6230', 62, 17, 9], 'cotija': ['DRY4128', 95, 16, 5], 'manchego': ['DRY8027', 47, 11, 3]}
        cheeses = ProductCat('cheese', cheese_inventory)
        cheeses.view_inventory()
        mock_patch.assert_called_with('''manchego: ['DRY8027', 47, 11, 3]''')
        assert mock_patch.call_count == 16


# CHEESES
@pytest.mark.describe('it returns correct instance & class attribute values & method output per arg input')
class TestProductCat(TestCase):
    def test_init(self):
        c = Cheese('DRY6282', 'mascarpone', 52, 16, 4)
        assert c.sku == 'DRY6282'
        assert c.name == 'mascarpone'
        assert c.stock == 52
        assert c.retail_price == 16
        assert c.wholesale_price == 4
        assert c.profit_margin == 12