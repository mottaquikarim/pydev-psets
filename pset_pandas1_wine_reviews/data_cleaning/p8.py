"""
Cleaning Data VIII - Find Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.

