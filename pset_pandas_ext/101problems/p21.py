"""
21. How to convert a series of date-strings to a timeseries?
"""
"""
Difficiulty Level: L2
"""
"""
Input
"""
"""
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
"""
"""
Desired Output
"""
"""
0   2010-01-01 00:00:00
1   2011-02-02 00:00:00
2   2012-03-03 00:00:00
3   2013-04-04 00:00:00
4   2014-05-05 00:00:00
5   2015-06-06 12:20:00
dtype: datetime64[ns]
"""
