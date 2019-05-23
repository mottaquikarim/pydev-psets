"""
Basic List Operations I
"""

# Create a list including these five animals - elephant, tiger, otter, orangutan, and penguin.

animals = ['elephant', 'tiger', 'rattlesnake', 'orangutan', 'penguin']


# Print the 4th animal on the list.
print(animals[3])


# Add 'tortoise' to the beginning of the list.
print(animals.insert(0,'tortoise'))


# Print the length of the list.
print(len(animals))


# Remove 'orangutan' from the list.
print(animals.pop(4))


# Sort the list alphabetically and print it out.
print(sorted(animals))

