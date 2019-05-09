"""
4. How to combine many series to form a dataframe?
"""
"""
Difficulty Level: L1
"""
"""
Combine ser1 and ser2 to form a dataframe.
"""
"""
Input
"""
"""
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
"""

# Input
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution 1
df = pd.concat([ser1, ser2], axis=1)

# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head())