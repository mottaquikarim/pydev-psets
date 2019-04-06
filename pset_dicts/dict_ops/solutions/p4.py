"""
Inverting Keys & Values - SOLUTION
"""

# Invert dict1 - make the current keys into values and the current values into keys.


dict1 = { "k1" : "v1", "k2" : "v2", "k3" : "v1" }

a = dict1.keys()
b = dict1.values()

dict1 = dict(zip(b, a))


print(dict1)
# {'v1': 'k3', 'v2': 'k2'}

