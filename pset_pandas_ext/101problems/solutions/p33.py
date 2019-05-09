"""
33. How to import only every nth row from a csv file to create a dataframe?
"""
"""
Difficiulty Level: L2
"""
"""
Import every 50th row of BostonHousing dataset as a dataframe.
"""
"""
 
"""

# Solution 1: Use chunks and for-loop
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2 = pd.DataFrame()
for chunk in df:
    df2 = df2.append(chunk.iloc[0,:])


# Solution 2: Use chunks and list comprehension
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2 = pd.concat([chunk.iloc[0] for chunk in df], axis=1)
df2 = df2.transpose()

# Solution 3: Use csv reader
import csv          
with open('BostonHousing.csv', 'r') as f:
    reader = csv.reader(f)
    out = []
    for i, row in enumerate(reader):
        if i%50 == 0:
            out.append(row)

df2 = pd.DataFrame(out[1:], columns=out[0])
print(df2.head())