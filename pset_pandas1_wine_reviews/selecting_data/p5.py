"""
Selecting Data V - Subsets
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Create a new dataframe called "wine_ratings" that is a subset of wine_reviews. It should have these columns in this order:
### title
### country
### points
### price