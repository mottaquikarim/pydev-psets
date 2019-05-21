"""
Data Organization III - Sorting a DataFrame by Multiple Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this DataFrame, sort the rows first, alphabetically by 'country', and second, by 'rating' from highest to lowest.

ratings_by_location = wine_reviews[['country', 'province', 'rating']]



# Take a look at the result by printing out the rows from indeces 0 to 10 as well as the rows from indeces 52065 to 52075.
