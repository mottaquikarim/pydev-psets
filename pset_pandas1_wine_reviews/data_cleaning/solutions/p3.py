"""
Data Cleaning III - Bulk Replace in a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Using this Series, replace all instances of 'US' with 'DEMOCRATIC REPUBLIC OF CONGO'.

countries = wine_reviews['country']

countries = countries.replace('US', 'DEMOCRATIC REPUBLIC OF CONGO', inplace=True)
print(countries.head(10))
"""
0                           Italy
1                        Portugal
2    DEMOCRATIC REPUBLIC OF CONGO
3    DEMOCRATIC REPUBLIC OF CONGO
4    DEMOCRATIC REPUBLIC OF CONGO
5                           Spain
6                           Italy
7                          France
8                         Germany
9                          France
"""

# Again using the original Series, replace all instances of 'US' with 'MADAGASCAR' and all instances of 'Italy' with 'DEMOCRATIC REPUBLIC OF CONGO'.

countries = wine_reviews['country']

countries = countries.replace(['US', 'Italy'], ['MADAGASCAR', 'DEMOCRATIC REPUBLIC OF CONGO'])
print(countries.head(10), inplace=True)
"""
0    DEMOCRATIC REPUBLIC OF CONGO
1                        Portugal
2                      MADAGASCAR
3                      MADAGASCAR
4                      MADAGASCAR
5                           Spain
6    DEMOCRATIC REPUBLIC OF CONGO
7                          France
8                         Germany
9                          France
"""
