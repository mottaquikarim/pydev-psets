"""
Data Cleaning III - Bulk Replace in a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this Series, replace all instances of 'US' with 'DEMOCRATIC REPUBLIC OF CONGO'.

countries = wine_reviews['country']



# Again using the original Series, replace all instances of 'US' with 'FRENCH POLYNESIA' and all instances of 'Italy' with 'MADAGASCAR'.