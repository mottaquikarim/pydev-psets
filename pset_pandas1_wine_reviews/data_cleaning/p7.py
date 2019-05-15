"""
Cleaning Data VII - View Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]



# Return a dataframe of booleans that show True for null values.



# Return a dataframe of booleans that show True for values that exist.
