"""
Data Cleaning V - Bulk Replace in a Single DataFrame Column (Like a Dict)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances of 'US' in the 'country' column with 'CZECH REPUBLIC'.

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]


wine_geography.replace({'country': {'US': 'CZECH REPUBLIC'}}, inplace=True)

print(wine_geography.head(10))
"""
              variety         country           province
0         White Blend           Italy  Sicily & Sardinia
1      Portuguese Red        Portugal              Douro
2          Pinot Gris  CZECH REPUBLIC             Oregon
3            Riesling  CZECH REPUBLIC           Michigan
4          Pinot Noir  CZECH REPUBLIC             Oregon
5  Tempranillo-Merlot           Spain     Northern Spain
6            Frappato           Italy  Sicily & Sardinia
7      Gewürztraminer          France             Alsace
8      Gewürztraminer         Germany        Rheinhessen
9          Pinot Gris          France             Alsace
"""

# Again using the original DataFrame, replace all instances of 'US' in the 'country' column with 'COSTA RICA' and all instances of 'Italy' with 'CZECH REPUBLIC'.

wine_geography = wine_reviews[['variety', 'country', 'province']]


wine_geography.replace({'country': {'US': 'INDONESIA', 'Italy': 'CZECH REPUBLIC'}}, inplace=True)

print(wine_geography.head(10))
"""
              variety         country           province
0         White Blend  CZECH REPUBLIC  Sicily & Sardinia
1      Portuguese Red        Portugal              Douro
2          Pinot Gris       INDONESIA             Oregon
3            Riesling       INDONESIA           Michigan
4          Pinot Noir       INDONESIA             Oregon
5  Tempranillo-Merlot           Spain     Northern Spain
6            Frappato  CZECH REPUBLIC  Sicily & Sardinia
7      Gewürztraminer          France             Alsace
8      Gewürztraminer         Germany        Rheinhessen
9          Pinot Gris          France             Alsace
"""

