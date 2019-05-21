"""
Data Cleaning VI - Bulk Replace Across Multiple DataFrame Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances in the following columns according to the directions below. HINT: You should be able to do this in one function call!
## 'country' column
#### 'US' should become 'Morocco'
#### 'France' should become 'Mexico'
## 'province' column
#### 'Oregon' should become 'Ouezzane'
#### 'Michigan' should become 'Fahs-Anjra'
#### 'Sicily & Sardinia' should become 'Tuscany'

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]

