"""
Fromagerie I - Create Inventory
"""


import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p1 import *


@patch("p1.random.randint")
@pytest.mark.describe('it returns randomly generated sku, stock #, retail price, & wholesale price')
def test_create_inventory(mock_random):
    def mock_randint(a, b):
        return a + 1

    mock_random.side_effect = mock_randint
    
    cheese_types = [
'brie',
'feta',
'cheddar',
'mozzarella',
'ricotta',
'provolone',
'gruyere',
'pecorino romano',
'parmigiano reggiano',
'gorgonzola',
'pepper jack',
'gouda',
'asiago',
'mascarpone',
'cotija',
'manchego'
]
    
    assert create_inventory(cheese_types) == {'brie': ['DRY8900', 27, 11, 5], 'feta': ['DRY7730', 74, 13, 9], 'cheddar': ['DRY3673', 2, 15, 1], 'mozzarella': ['DRY7506', 17, 13, 3], 'ricotta': ['DRY9723', 60, 14, 3], 'provolone': ['DRY5895', 55, 14, 7], 'gruyere': ['DRY3934', 49, 11, 4], 'pecorino romano': ['DRY9980', 24, 10, 8], 'parmigiano reggiano': ['DRY1601', 79, 10, 0], 'gorgonzola': ['DRY6408', 72, 18, 8], 'pepper jack': ['DRY2506', 85, 10, 9], 'gouda': ['DRY4270', 83, 15, 9], 'asiago': ['DRY1592', 42, 18, 2], 'mascarpone': ['DRY6230', 62, 17, 9], 'cotija': ['DRY4128', 95, 16, 5], 'manchego': ['DRY8027', 47, 11, 3]}