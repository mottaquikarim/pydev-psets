"""
72. How to get the positions where values of two columns match?
"""
"""
Difficulty Level: L2
"""
"""
 
"""

# Input
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                    'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})

# Solution
np.where(df.fruit1 == df.fruit2)