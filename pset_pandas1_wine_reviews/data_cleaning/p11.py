"""
Cleaning Data XI - Removing Duplicates
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Using this DataFrame, drop the null values in the 'price' and 'country' columns. Then find the number of duplicates values in the 'title' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]




# Now, drop the duplicate rows in the 'title' column.




# Print out these statements with the correct values for the blanks.


# _____ rows w. null values removed
# _____ duplicate rows removed
# _____ total rows removed