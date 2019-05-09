"""
55. How to reshape a dataframe to the largest possible square after removing the negative values?
"""
"""
Difficulty Level: L3
"""
"""
Reshape df to the largest possible square with negative values removed. Drop the smallest values if need be. The order of the positive numbers in the result should remain the same as the original.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
"""

# Input
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
print(df)

# Solution
# Step 1: remove negative values from arr
arr = df[df > 0].values.flatten()
arr_qualified = arr[~np.isnan(arr)]

# Step 2: find side-length of largest possible square
n = int(np.floor(arr_qualified.shape[0]**.5))

# Step 3: Take top n^2 items without changing positions
top_indexes = np.argsort(arr_qualified)[::-1]
output = np.take(arr_qualified, sorted(top_indexes[:n**2])).reshape(n, -1)
print(output)