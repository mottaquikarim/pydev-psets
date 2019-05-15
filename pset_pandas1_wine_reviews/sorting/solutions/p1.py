"""
Data Organization I - Sorting a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Using this Series, sort the elements alphabetically.

countries = wine_reviews['country']

countries = countries.sort_values()
print(countries.head())

"""
90901     Argentina
122372    Argentina
122374    Argentina
4814      Argentina
4806      Argentina
"""

# Using this Series, sort the elements from highest to lowest.

prices = wine_reviews['price']

prices = prices.sort_values(ascending = False)
print(prices.head())

"""
80290     3300.0
15840     2500.0
98380     2500.0
120391    2013.0
113564    2000.0
"""