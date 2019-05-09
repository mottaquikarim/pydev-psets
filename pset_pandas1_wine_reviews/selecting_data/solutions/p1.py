"""
Selecting Data I - Access a Row
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')


# Return the 12th row in the wine_reviews dataframe.

print(wine_reviews.iloc[12,:])

"""
country                                                                 US
description              Slightly reduced, this wine offers a chalky, t...
designation                                                            NaN
points                                                                  87
price                                                                   34
province                                                        California
region_1                                                  Alexander Valley
region_2                                                            Sonoma
taster_name                                                 Virginie Boone
taster_twitter_handle                                              @vboone
title                    Louis M. Martini 2012 Cabernet Sauvignon (Alex...
variety                                                 Cabernet Sauvignon
winery                                                    Louis M. Martini
"""