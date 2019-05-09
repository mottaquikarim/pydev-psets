"""
Selecting Data VI - Min & Max (CHALLENGE!)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Find the 5 rows with the highest-priced wine and the 5 rows with the lowest-priced wine. Assign them to variables called 'a' and 'b' respectively. Print 'a' and 'b'.
a = wine_reviews.nlargest(5, 'price')
b = wine_reviews.nsmallest(5, 'price')

print(a, '\n\n', b)

# Create a function to print out the variety and price of some number of the most and least expensive wines. Hints:
### It should contain loops
### The number function should take any number for finding the highest and lowest priced wines (e.g. top and bottom 5, top and bottom 10, etc.)
### If you're iterating through a 2 column dataframe item by item, remember the counting goes like this:
"""
[0,0], [0,1]
[1,0], [1,1]
[2,0], [2,1]
[3,0], [3,1]
[4,0], [4,1]
"""

def high_low_prices(high, low, limit):
    """
    prints out the variety & price of the top 5 
    """

    # high
    print('Most Expensive Wines by Variety')
    row_count = 0
    col1 = 0
    col2 = 1
    while row_count < limit:
        #print(f'[{row_count}, {col1}] & [{row_count}, {col2}]')
        print(f'{high.iloc[row_count,col1]} - ${high.iloc[row_count,col2]}')
        row_count += 1

    print('\n')

    # low
    print('Cheapest Wines by Variety')
    row_count = 0
    col1 = 0
    col2 = 1
    while row_count < limit:
        #print(f'[{row_count}, {col1}] & [{row_count}, {col2}]')
        print(f'{high.iloc[row_count,col1]} - ${high.iloc[row_count,col2]}')
        row_count += 1

    return None

limit = 5
a = wine_reviews.nlargest(limit, 'price')
b = wine_reviews.nsmallest(limit, 'price')

high = a[['variety', 'price']]
low = b[['variety', 'price']]

high_low_prices(high, low, limit)

"""
Most Expensive Wines by Variety
Bordeaux-style Red Blend - $3300.0
Bordeaux-style Red Blend - $2500.0
Pinot Noir - $2500.0
Chardonnay - $2013.0
Bordeaux-style Red Blend - $2000.0


Cheapest Wines by Variety
Bordeaux-style Red Blend - $3300.0
Bordeaux-style Red Blend - $2500.0
Pinot Noir - $2500.0
Chardonnay - $2013.0
Bordeaux-style Red Blend - $2000.0
"""

