"""
Data Cleaning II - Rename Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Rename the 'designation' column to 'vineyard' and the 'points' column to 'rating'.
