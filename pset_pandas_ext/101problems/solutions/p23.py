"""
23. How to convert year-month string to dates corresponding to the 4th day of the month?
"""
"""
Difficiulty Level: L2
"""
"""
Change ser to dates that start with 4th of the respective months.
"""
"""
Input
"""
"""
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
"""
"""
Desired Output
"""
"""
0   2010-01-04
1   2011-02-04
2   2012-03-04
dtype: datetime64[ns]
"""

import pandas as pd
# Input
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

# Solution 1
from dateutil.parser import parse
# Parse the date
ser_ts = ser.map(lambda x: parse(x))

# Construct date string with date as 4
ser_datestr = ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'

# Format it.
[parse(i).strftime('%Y-%m-%d') for i in ser_datestr]

# Solution 2
ser.map(lambda x: parse('04 ' + x))