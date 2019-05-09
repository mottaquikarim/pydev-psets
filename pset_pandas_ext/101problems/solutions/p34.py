"""
34. How to change column values when importing csv to a dataframe?
"""
"""
Difficulty Level: L2
"""
"""
Import the boston housing dataset, but while importing change the 'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.
"""
"""
 
"""

# Solution 1: Using converter parameter
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', 
                 converters={'medv': lambda x: 'High' if float(x) > 25 else 'Low'})


# Solution 2: Using csv reader
import csv
with open('BostonHousing.csv', 'r') as f:
    reader = csv.reader(f)
    out = []
    for i, row in enumerate(reader):
        if i > 0:
            row[13] = 'High' if float(row[13]) > 25 else 'Low'
        out.append(row)

df = pd.DataFrame(out[1:], columns=out[0])
print(df.head())