"""
Data Cleaning IV - Bulk Replace in a DataFrame
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Using this DataFrame, replace all instances of 'US' with 'UNITED ARAB EMIRATES'.

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]


wine_geography.replace({'country': {'US': 'UNITED ARAB EMIRATES'}}, inplace=True)

print(wine_geography.head(10))
"""
              variety               country           province
0         White Blend                 Italy  Sicily & Sardinia
1      Portuguese Red              Portugal              Douro
2          Pinot Gris  UNITED ARAB EMIRATES             Oregon
3            Riesling  UNITED ARAB EMIRATES           Michigan
4          Pinot Noir  UNITED ARAB EMIRATES             Oregon
5  Tempranillo-Merlot                 Spain     Northern Spain
6            Frappato                 Italy  Sicily & Sardinia
7      Gewürztraminer                France             Alsace
8      Gewürztraminer               Germany        Rheinhessen
9          Pinot Gris                France             Alsace
"""

# Again using the original DataFrame, replace all instances of 'US' in the 'country' column with 'COSTA RICA' and all instances of 'Italy' with 'UNITED ARAB EMIRATES'.

wine_geography = wine_reviews[['variety', 'country', 'province']]

wine_geography['country'].replace(['US', 'Italy'], ['COSTA RICA', 'UNITED ARAB EMIRATES'], inplace=True)

print(wine_geography.head(10))
"""
              variety               country           province
0         White Blend  UNITED ARAB EMIRATES  Sicily & Sardinia
1      Portuguese Red              Portugal              Douro
2          Pinot Gris            COSTA RICA             Oregon
3            Riesling            COSTA RICA           Michigan
4          Pinot Noir            COSTA RICA             Oregon
5  Tempranillo-Merlot                 Spain     Northern Spain
6            Frappato  UNITED ARAB EMIRATES  Sicily & Sardinia
7      Gewürztraminer                France             Alsace
8      Gewürztraminer               Germany        Rheinhessen
9          Pinot Gris                France             Alsace
"""