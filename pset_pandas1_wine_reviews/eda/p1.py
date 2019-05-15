"""
Exploratory Data Analysis I - Core Stats Summary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')




print(wine_reviews.describe())

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]

print(wine_ratings.describe())