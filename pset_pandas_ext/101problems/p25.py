"""
25. How to filter valid emails from a series?
"""
"""
Difficiulty Level: L3
"""
"""
Extract the valid emails from the series emails. The regex pattern for valid emails is provided as reference.
"""
"""
Input
"""
"""
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
"""
"""
Desired Output
"""
"""
1    rameses@egypt.com
2            matt@t.co
3    narendra@modi.com
dtype: object
"""
