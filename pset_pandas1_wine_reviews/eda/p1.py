"""
Exploratory Data Analysis I - Core Stats Summary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# With one function call, return the core statistics for the wine_ratings DataFrame below.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Drop the null values in the latter three columns and drop duplicates based on the 'title' column. Then return the core statistics again.

