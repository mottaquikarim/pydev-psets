"""
Checking Imported Data III - DataFrame Labels
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')


# Access the labels on the rows of data.

print(wine_reviews.index) # RangeIndex(start=0, stop=129971, step=1)

# Access the labels on the columns of data.

print(wine_reviews.columns) # Index(['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'], dtype='object')

# Return the labels for the rows and columns in wine_reviews in one command.

print(wine_reviews.axes)
"""
[RangeIndex(start=0, stop=129971, step=1), Index(['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'], dtype='object')
"""