"""
2. How to create a series from a list, numpy array and dict?
"""
"""
Create a pandas series from each of the items below: a list, numpy and a dictionary
"""
"""
Input
"""
"""
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
"""

# Inputs
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser3.head())