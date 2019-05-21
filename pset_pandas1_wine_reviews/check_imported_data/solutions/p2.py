"""
Checking Imported Data II - How Big is the Data?
"""


import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')


# Print the number of rows and columns in wine_reviews.

print(wine_reviews.shape) # (rows, columns) is (129971, 13)

# Print the number of elements in wine_reviews.

print(wine_reviews.size) # 1689623