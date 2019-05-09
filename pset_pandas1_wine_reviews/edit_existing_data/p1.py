"""
Editing Existing Data I - Rename
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Rename the "designation" columns to "vineyard" and the "points" column to "rating".
