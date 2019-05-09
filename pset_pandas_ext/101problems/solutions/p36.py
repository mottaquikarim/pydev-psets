"""
36. How to import only specified columns from a csv file?
"""
"""
Difficulty Level: L1
"""
"""
Import ‘crim’ and ‘medv’ columns of the BostonHousing dataset as a dataframe.
"""
"""
 
"""

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', usecols=['crim', 'medv'])
print(df.head())