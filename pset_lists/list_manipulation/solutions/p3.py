"""
Merge Lists with Duplicates
"""

# Use the two lists below to solve this problem. Print out the result from each section as you go along.

list1, list2 = [2, 8, 6], [10, 4, 12]


# Add another instance of each item in list1 to list1 again and assign the results to list3.
list3 = list1 * 2
print(list3) # [2, 8, 6, 2, 8, 6]


# Combine the two given lists and assign them to list4.
list4 = list2 + list3
print(list4) # [10, 4, 12, 2, 8, 6, 2, 8, 6]


# Replace the first 3 items in list 3 with the numbers 13, 16, 9.
list3[:2] = [13, 16, 9]
print(list3) # [13, 16, 9, 6, 2, 8, 6]

# Create a variable list5. Merge list3 and list4 to create a list containing no duplicates.
list5 = set(list3 + list4)
list5 = list(list5)
print(list5) # [2, 4, 6, 8, 9, 10, 12, 13, 16]


# Take a look at your printed statements to see the evolution of your lists with each step of this problem.


