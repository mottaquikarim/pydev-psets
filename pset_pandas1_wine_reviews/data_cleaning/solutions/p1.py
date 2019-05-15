"""
Cleaning Data I - Drop Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Drop the 'region_2' and 'taster_twitter_handle' columns.

wine_reviews = wine_reviews.drop(columns=['region_2', 'taster_twitter_handle'])

print(wine_reviews.columns)
# Index(['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'taster_name', 'title', 'variety', 'winery'], dtype='object')