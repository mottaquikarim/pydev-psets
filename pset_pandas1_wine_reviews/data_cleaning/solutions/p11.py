"""
Cleaning Data XI - Removing Duplicates
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Using this DataFrame, drop the null values in the 'price' and 'country' columns. Then find the number of duplicates values in the 'title' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]
a = len(wine_ratings) # 129971 rows


wine_ratings = wine_ratings.dropna(subset=['country', 'price'])
b = len(wine_ratings) # 120916 rows

dups = wine_ratings.duplicated(['title']).sum() # 10333 dups



# Now, drop the duplicate rows in the 'title' column.

wine_ratings = wine_ratings.drop_duplicates(['title'])
c = len(wine_ratings) # 110583 rows



# Print out these statements with the correct values for the blanks.

print(f'{a-b} rows w. null values removed')
# 9055 rows w. null values removed
print(f'{b-c} duplicate rows removed')
# 10333 duplicate rows removed
print(f'{a-c} total rows removed')
# 19388 total rows removed