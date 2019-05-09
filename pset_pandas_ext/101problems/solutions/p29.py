"""
29. How to replace missing spaces in a string with the least frequent character?
"""
"""
Replace the spaces in my_str with the least frequent character.
"""
"""
Difficiulty Level: L2
"""
"""
Input
"""
"""
my_str = 'dbc deb abed gade'
"""
"""
Desired Output
"""
"""
'dbccdebcabedcgade'  # least frequent is 'c'
"""

# Input
my_str = 'dbc deb abed gade'

# Solution
ser = pd.Series(list('dbc deb abed gade'))
freq = ser.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
"".join(ser.replace(' ', least_freq))