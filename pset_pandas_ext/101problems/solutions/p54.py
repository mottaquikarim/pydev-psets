"""
54. How to find and cap outliers from a series or dataframe column?
"""
"""
Difficulty Level: L2
"""
"""
Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 5th and 95th %ile value.
"""
"""
Input
"""
"""
ser = pd.Series(np.logspace(-2, 2, 30))
"""

# Input
ser = pd.Series(np.logspace(-2, 2, 30))

# Solution
def cap_outliers(ser, low_perc, high_perc):
    low, high = ser.quantile([low_perc, high_perc])
    print(low_perc, '%ile: ', low, '|', high_perc, '%ile: ', high)
    ser[ser < low] = low
    ser[ser > high] = high
    return(ser)

capped_ser = cap_outliers(ser, .05, .95)