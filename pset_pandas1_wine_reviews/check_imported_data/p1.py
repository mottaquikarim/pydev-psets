"""
Checking Imported Data I - Data Dictionary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Access a summary of the core metadata of the DataFrame (i.e. the number and name of columns, the rows, etc.)