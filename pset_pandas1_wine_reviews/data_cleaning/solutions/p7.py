"""
Cleaning Data VII - View Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]



# Return a dataframe of booleans that show True for null values.
print(wine_ratings.isnull())
"""
first 3 rows are:

   title  country  points  price
0  False    False   False   True
1  False    False   False  False
2  False    False   False  False
"""


# Return a dataframe of booleans that show True for values that exist.
print(wine_ratings.notnull())
"""
first 3 rows are:

    title  country  points  price
0   True     True    True  False
1   True     True    True   True
2   True     True    True   True
"""