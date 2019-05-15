"""
Data Organization II - Sorting a DataFrame
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Using this DataFrame, sort the rows reverse alphabetically based on the 'country' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]

wine_ratings = wine_ratings.sort_values('country', ascending = False)
print(wine_ratings.head())

"""
                                                    title  country  rating  price
97552     Pisano 2013 Cisplatino Tannat-Merlot (Progreso)  Uruguay      86   12.0
113525   Garzón 2015 Single Vineyard Pinot Noir (Uruguay)  Uruguay      90   30.0
10527   Pueblo del Sol 2009 30 Barricas Edición Limita...  Uruguay      90   29.0
128760  Pizzorno 2013 Select Blend Reserva Red (Canelo...  Uruguay      90   20.0
10532                    Bouza 2013 Albariño (Montevideo)  Uruguay      90   25.0
"""


# Now sort the DataFrame's rows based on price from highest to lowest.

wine_ratings = wine_ratings.sort_values('price')
print(wine_ratings.head())

"""
                                                    title  country  rating  price
1987    Felix Solis 2013 Flirty Bird Syrah (Vino de la...    Spain      85    4.0
59507     Pam's Cuties NV Unoaked Chardonnay (California)       US      83    4.0
31530                   Bandit NV Chardonnay (California)       US      84    4.0
117303  Felix Solis 2012 Flirty Bird White (Vino de la...    Spain      82    4.0
126096  Cramele Recas 2011 UnWineD Pinot Grigio (Viile...  Romania      86    4.0
"""