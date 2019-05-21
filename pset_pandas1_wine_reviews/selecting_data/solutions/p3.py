"""
Selecting Data III - Access Single Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# Print the value in the 5th column of the 7th row.
print(wine_reviews.iloc[6,5]) # Sicily & Sardinia


# Create a Series called "countries" from the 'country' column and print item at index 18.
countries = wine_reviews['country']
print(countries.iloc[18]) # Spain


# Print the 10th item in countries.
print(countries.loc[9]) # France

