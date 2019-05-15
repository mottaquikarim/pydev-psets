"""
Cleaning Data X - Fill Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]



# Replace all the null 'price' values with the mean of the existing 


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.


# Replace all the missing values in the 'country' column with 'Unknown'. Hint: Remember this should be the only column left with null values.


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.


