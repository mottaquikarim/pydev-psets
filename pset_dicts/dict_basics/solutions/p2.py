"""
Predators & Prey
"""

# A) Create a dict called "pred_prey", containing:
### 3 carnivorous marine animals
### For each carnivore, 3 examples of its prey

pred_prey = {
    'dolphin': ['shrimp', 'herring', 'squid'],
    'orca whale': ['sea turtle', 'harp seal', 'squid'],
    'great white shark': ['sea lion', 'sea turtle', 'harp seal']
}

# B) Print out the 2nd predator and its prey in this format:
#### predator2: prey1, prey2, & prey3

items = list(pred_prey.items())
print(f'{items[1][0]}: {items[1][1][0]}, {items[1][1][1]}, & {items[1][1][2]}')


# C) Print a unique collection of all the prey in a variable called "prey".

prey_lists = list(pred_prey.values())

prey = []
prey.extend(prey_lists[0])
prey.extend(prey_lists[1])
prey.extend(prey_lists[2])

prey = set(prey)
print(prey)