"""
Basic List Operations I
"""

# A) Create a list including these five animals - elephant, tiger, otter, orangutan, and penguin.

animals = ['elephant', 'tiger', 'rattlesnake', 'orangutan', 'penguin']
print('A)', animals) # ['elephant', 'tiger', 'rattlesnake', 'orangutan', 'penguin']

# B) Print the 4th animal on the list.
print('B)', animals[3]) # orangutan


# C) Add 'tortoise' to the beginning of the list.
animals.insert(0,'tortoise')
print('C)', animals) # ['tortoise', 'elephant', 'tiger', 'rattlesnake', 'orangutan', 'penguin']


# D) Print the length of the list.
print('D)', len(animals)) # 6


# E) Remove 'orangutan' from the list.
print('E)', animals.pop(4)) # orangutan
print(animals) # ['tortoise', 'elephant', 'tiger', 'rattlesnake', 'penguin']


# F) Sort the list alphabetically and print it out.
print('F)', sorted(animals)) # ['elephant', 'penguin', 'rattlesnake', 'tiger', 'tortoise']
