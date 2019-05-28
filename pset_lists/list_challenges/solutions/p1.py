"""
CHALLENGE - Extensions
"""

# ** Challenge** Add each element of the tuple1 to list1 *individually* and print the result.

list1 = [6, 12, 9, 4, 10, 1]
tuple1 = [(15,3), (6,2), (1, 8)]

list2 = []
list2.extend(tuple1[0])
list2.extend(tuple1[1])
list2.extend(tuple1[2])


list1.extend(list2)
print(list1)

