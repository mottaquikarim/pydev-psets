"""
Cleaning Data I - Drop Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Drop the 'region_2' and 'taster_twitter_handle' columns.
