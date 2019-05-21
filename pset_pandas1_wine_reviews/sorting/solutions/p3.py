"""
Data Organization III - Sorting a DataFrame by Multiple Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# Using this DataFrame, sort the rows first, alphabetically by 'country', and second, by 'rating' from highest to lowest.

ratings_by_location = wine_reviews[['country', 'province', 'rating']]


ratings_by_location = ratings_by_location.sort_values(['country', 'rating'], ascending= [True, False])



# Take a look at the result by printing out the rows from indeces 0 to 10 as well as the rows from indeces 52065 to 52075.

print(ratings_by_location.iloc[0:10], '\n\n', ratings_by_location.iloc[52065:52075])
"""
          country          province  rating
82754   Argentina  Mendoza Province      97
109230  Argentina  Mendoza Province      96
109840  Argentina  Mendoza Province      96
8869    Argentina  Mendoza Province      95
38984   Argentina  Mendoza Province      95
78302   Argentina  Mendoza Province      95
78303   Argentina             Other      95
88861   Argentina  Mendoza Province      95
95070   Argentina  Mendoza Province      95
122027  Argentina  Mendoza Province      95

        country           province  rating
129803   Italy             Veneto      88
129804   Italy             Veneto      88
129826   Italy           Piedmont      88
0        Italy  Sicily & Sardinia      87
6        Italy  Sicily & Sardinia      87
13       Italy  Sicily & Sardinia      87
22       Italy  Sicily & Sardinia      87
24       Italy  Sicily & Sardinia      87
26       Italy  Sicily & Sardinia      87
27       Italy  Sicily & Sardinia      87
"""