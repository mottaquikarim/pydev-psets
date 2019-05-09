"""
Simple Series
"""


# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np


# simple array
data = np.array(['l', 'a', 'y', 'l', 'a'])

# convert data to series
ser = pd.Series(data)
print(ser)


# grab the first three items from ser
sub = ser[:3]
print(sub)


# create series with custom label such that:
"""
a    l
b    a
c    y
d    l
e    a
dtype: object
"""
ser2 = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(ser2)

# access "y" from series ser2
print("accessing 'y'", ser2['c'])
