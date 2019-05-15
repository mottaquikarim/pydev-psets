"""
Exploratory Data Analysis II - Unique Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Print a list of all the unique countries in the wine_reviews DataFrame in alphabetical order. Also print the number of unique countries that exist in the dataset. Hint: Don't just find the length of your first result.

countries = wine_reviews['country']
unique_countries = countries.unique()
unique_countries.sort()

print(f'There are {countries.nunique()} unique countries: \n', unique_countries) 
"""
There are 42 unique countries:
['Argentina' 'Armenia' 'Australia' 'Austria' 'Bosnia and Herzegovina'
 'Brazil' 'Bulgaria' 'Canada' 'Chile' 'China' 'Croatia' 'Cyprus'
 'Czech Republic' 'England' 'France' 'Georgia' 'Germany' 'Greece'
 'Hungary' 'India' 'Israel' 'Italy' 'Lebanon' 'Luxembourg' 'Macedonia'
 'Mexico' 'Moldova' 'Morocco' 'New Zealand' 'Peru' 'Portugal' 'Romania'
 'Serbia' 'Slovakia' 'Slovenia' 'South Africa' 'Spain' 'Switzerland'
 'Turkey' 'US' 'Ukraine' 'Uruguay']
"""