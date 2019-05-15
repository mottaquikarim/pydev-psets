"""
Cleaning Data V - Fill Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Replace all the null 'price' values with the mean of the existing 

prices = wine_reviews['price']
m = prices.mean()
replace_value = {'price': prices.mean()}
wine_ratings = wine_ratings.fillna(value=replace_value)


# Return a count of the null values in wine_ratings.
print(wine_ratings.isnull().sum())
"""
title       0
country    63
rating      0
price       0
"""


# Print out the number of rows in wine_ratings.
print(len(wine_ratings)) # 129971


# Replace all the missing values in the 'country' column with 'Unknown'. Hint: Remember this should be the only column left with null values.
wine_ratings = wine_ratings.fillna(value='Unknown')


# Return a count of the null values in wine_ratings.
print(wine_ratings.isnull().sum())
"""
title       0
country     0
rating      0
price       0
"""

# Print out the number of rows in wine_ratings.
print(len(wine_ratings)) # 129971


