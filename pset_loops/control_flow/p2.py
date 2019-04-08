"""
Control Flow II
"""

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement. 

for i in range(6):
    if (i == 3 or i ==6):
        continue
    print(i,end=' ')
print("\n")