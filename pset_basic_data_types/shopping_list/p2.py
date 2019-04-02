"""
Shopping List Calculator II
"""

from pset_basic_data_types.shopping_list.p1 import *

# Given the item names and prices from p1.py
# calculate the total price and price with tax.

TAX_RATE = 8.875  # this is a percentage!

total = None
tax = None
total_total = None

# Sample output:
'''
1 Coco Puffs = $8.95.
2 Pop tarts = $5.00. # this means price of pop tarts is 2.50
1 Eggs = $3.25.
1 Steak = $12.00
1 Milk = $2.25.
TOTAL: $31.45 # this is calculated by adding the above
TAX: $2.594625. # this is calculated by 8.875% of TOTAL
TOTAL TOTAL: $34.04 # use round() to solve this
'''
