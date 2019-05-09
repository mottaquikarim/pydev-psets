"""
Checking Imported Data IV - Preview Data
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Print out the first and last 3 rows of data.

print(wine_reviews.head(3))
"""
    country  ...               winery
0     Italy  ...              Nicosia
1  Portugal  ...  Quinta dos Avidagos
2        US  ...            Rainstorm
"""
print(wine_reviews.tail(3))
"""
        country  ...                winery
129968   France  ...       Domaine Gresser
129969   France  ...  Domaine Marcel Deiss
129970   France  ...      Domaine Schoffit

[3 rows x 13 columns]
"""