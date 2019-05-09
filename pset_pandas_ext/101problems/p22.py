"""
22. How to get the day of month, week number, day of year and day of week from a series of date strings?
"""
"""
Difficiulty Level: L2
"""
"""
Get the day of month, week number, day of year and day of week from ser.
"""
"""
Input
"""
"""
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
"""
"""
Desired output
"""
"""
Date:  [1, 2, 3, 4, 5, 6]
Week number:  [53, 5, 9, 14, 19, 23]
Day num of year:  [1, 33, 63, 94, 125, 157]
Day of week:  ['Friday', 'Wednesday', 'Saturday', 'Thursday', 'Monday', 'Saturday']
"""
