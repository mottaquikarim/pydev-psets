"""
Data Organization II - Sorting a DataFrame
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Using this DataFrame, sort the rows reverse alphabetically based on the 'country' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]




# Now sort the DataFrame's rows based on price from highest to lowest.

