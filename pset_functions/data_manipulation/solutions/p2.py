"""
Clean Pairs
"""

# Below is a list of common food pairings. Write a function called "cleaner" that cleans the data such that each list item is a tuple (e.g. ('Milk', 'Cookies')). Assign the results to a variable called "clean_pairs".

pairs = [('Milk', 'Cookies'), ('Peanut Butter - Jelly'), ('Spaghetti & Meatballs'), ('Eggs', 'Bacon'), ('Pancakes & Syrup'), ('Chicken - Waffles'), ('Peas', 'Carrots')]

def cleaner(data):
  for item in pairs:
    if '-' in item:
      idx = pairs.index(item)
      x = tuple(item.split(' - '))
      pairs.remove(item)
      pairs.insert(idx,x)
    elif '&' in item:
      idx = pairs.index(item)
      y = tuple(item.split(' & '))
      pairs.remove(item)
      pairs.insert(idx,y)

  return pairs

clean_pairs = cleaner(pairs)
print(clean_pairs)