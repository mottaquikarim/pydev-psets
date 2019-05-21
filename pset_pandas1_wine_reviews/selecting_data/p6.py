"""
Selecting Data VI - Min & Max (CHALLENGE!)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Find the 5 rows with the highest-priced wine and the 5 rows with the lowest-priced wine. Assign them to variables called 'a' and 'b' respectively. Print 'a' and 'b'.



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

