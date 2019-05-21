"""
Selecting Data V - Subsets
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# Create a new dataframe called "wine_ratings" that is a subset of wine_reviews. It should have these columns in this order:
### title
### country
### points
### price


wine_ratings = wine_reviews[['title', 'country', 'points', 'price']]

# Print out the number of rows and columns in wine_ratings.
print(wine_ratings.shape) # (129971, 4)


# Print out the first 10 rows of wine_ratings.
print(wine_ratings.head(10))
"""
                                               title   country  points  price
0                  Nicosia 2013 Vulkà Bianco  (Etna)     Italy      87    NaN
1      Quinta dos Avidagos 2011 Avidagos Red (Douro)  Portugal      87   15.0
2      Rainstorm 2013 Pinot Gris (Willamette Valley)        US      87   14.0
3  St. Julian 2013 Reserve Late Harvest Riesling ...        US      87   13.0
4  Sweet Cheeks 2012 Vintner's Reserve Wild Child...        US      87   65.0
5  Tandem 2011 Ars In Vitro Tempranillo-Merlot (N...     Spain      87   15.0
6   Terre di Giurfo 2013 Belsito Frappato (Vittoria)     Italy      87   16.0
7              Trimbach 2012 Gewurztraminer (Alsace)    France      87   24.0
8  Heinz Eifel 2013 Shine Gewürztraminer (Rheinhe...   Germany      87   12.0
9  Jean-Baptiste Adam 2012 Les Natures Pinot Gris...    France      87   27.0
"""

