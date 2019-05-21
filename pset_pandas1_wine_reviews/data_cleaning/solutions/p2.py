"""
Data Cleaning II - Rename Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# Rename the 'designation' column to 'vineyard' and the 'points' column to 'rating'.

wine_reviews.rename(columns={'designation': 'vineyard', 'points': 'rating'}, inplace=True)

print(wine_reviews.columns)
# Index(['country', 'description', 'vineyard', 'rating', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'], dtype='object')