"""
Data Cleaning IV - Bulk Replace in a Single DataFrame Column (Like a Series)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances of 'US' in the 'country' column with 'UNITED ARAB EMIRATES'.

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]



# Again using the original DataFrame, replace all instances of 'US' in the 'country' column with 'COSTA RICA' and all instances of 'Italy' in the 'country' column with 'UNITED ARAB EMIRATES'.



