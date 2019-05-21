"""
Data Cleaning VI - Bulk Replace Across Multiple DataFrame Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances in the following columns according to the directions below. HINT: You should be able to do this in one function call!
## 'country' column
#### 'US' should become 'Morocco'
#### 'France' should become 'Mexico'
## 'province' column
#### 'Oregon' should become 'Ouezzane'
#### 'Michigan' should become 'Fahs-Anjra'
#### 'Sicily & Sardinia' should become 'Tuscany'

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]


wine_geography.replace({
	'country': {'US': 'Morocco', 'France': 'Mexico'},
	'province': {'Oregon': 'Ouezzane', 'Michigan': 'Fahs-Anjra', 'Sicily & Sardinia': 'Tuscany'}
	}, inplace=True)

print(wine_geography.head(10))
"""
              variety   country        province
0         White Blend     Italy         Tuscany
1      Portuguese Red  Portugal           Douro
2          Pinot Gris   Morocco        Ouezzane
3            Riesling   Morocco      Fahs-Anjra
4          Pinot Noir   Morocco        Ouezzane
5  Tempranillo-Merlot     Spain  Northern Spain
6            Frappato     Italy         Tuscany
7      Gewürztraminer    Mexico          Alsace
8      Gewürztraminer   Germany     Rheinhessen
9          Pinot Gris    Mexico          Alsace
"""