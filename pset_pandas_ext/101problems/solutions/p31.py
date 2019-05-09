"""
31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?
"""
"""
Difficiulty Level: L2
"""
"""
ser has missing dates and values. Make all missing dates appear and fill up with value from previous date.
"""
"""
Input
"""
"""
ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
print(ser)
#> 2000-01-01     1.0
#> 2000-01-03    10.0
#> 2000-01-06     3.0
#> 2000-01-08     NaN
#> dtype: float64
"""
"""
Desired Output
"""
"""
2000-01-01     1.0
2000-01-02     1.0
2000-01-03    10.0
2000-01-04    10.0
2000-01-05    10.0
2000-01-06     3.0
2000-01-07     3.0
2000-01-08     NaN
"""

# Input
ser = pd.Series([1,10,3, np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))

# Solution
ser.resample('D').ffill()  # fill with previous value

# Alternatives
ser.resample('D').bfill()  # fill with next value
ser.resample('D').bfill().ffill()  # fill next else prev value