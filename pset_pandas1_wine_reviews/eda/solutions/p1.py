"""
Exploratory Data Analysis I - Core Stats Summary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)


# With one function call, return the core statistics for the wine_ratings DataFrame below.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]

print(wine_ratings.describe())
"""
              rating          price
count  129971.000000  120975.000000
mean       88.447138      35.363389
std         3.039730      41.022218
min        80.000000       4.000000
25%        86.000000      17.000000
50%        88.000000      25.000000
75%        91.000000      42.000000
max       100.000000    3300.000000
"""

# Drop the null values in the latter three columns and drop duplicates based on the 'title' column. Then return the core statistics again.

wine_ratings = wine_ratings.dropna(subset=['country', 'rating', 'price'])
wine_ratings = wine_ratings.drop_duplicates(['title'])


print(wine_ratings.describe())
"""
              rating          price
count  110583.000000  110583.000000
mean       88.416366      35.597985
std         3.100649      41.900380
min        80.000000       4.000000
25%        86.000000      17.000000
50%        88.000000      25.000000
75%        91.000000      42.000000
max       100.000000    3300.000000
"""

