"""
Data Organization I - Sorting a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this Series, sort the elements alphabetically.

countries = wine_reviews['country']



# Using this Series, sort the elements from highest to lowest.

prices = wine_reviews['price']