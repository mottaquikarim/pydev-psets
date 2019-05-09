"""
Selecting Data IV - Access Slices
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Print the first 3 values in the 'province' column.
print(wine_reviews['province'][:3])


# Create a Series called "provinces" and print the first 3 values.
provinces = wine_reviews['province']
print(provinces.iloc[:3])

"""
A & B both output:

0    Sicily & Sardinia
1                Douro
2               Oregon
"""