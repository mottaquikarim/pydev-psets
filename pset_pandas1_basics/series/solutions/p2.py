"""
Indexing and Selecting Series
"""

# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np

# create a new series
s = pd.Series(np.nan, index=[49, 48, 47, 46, 45, 1, 2, 3, 4, 5])

# using iloc, get the first 3 items in series
t = s.iloc[:3]

# using loc, do the same
u = s.loc[:47]

# using index operators, do the same
v = s[0:3]
