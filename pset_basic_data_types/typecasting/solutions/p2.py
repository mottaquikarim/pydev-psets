"""
Typcasting w. Strings
"""

# Convert these variables into strings and then back to their original data types. Print out each result as well as its data type. What do you notice about the last one?

five = 5
zero = 0
neg_8 = -8
T = True
F = False


five = str(five)
zero = str(zero)
neg_8 = str(neg_8)
T = str(T)
F = str(F)

print(five, type(five)) # '5' <class 'str'>
print(zero, type(zero)) # '0' <class 'str'>
print(neg_8, type(neg_8)) # '-8' <class 'str'>
print(T, type(T)) # 'True' <class 'str'>
print(F, type(F)) # 'False' <class 'str'>



five = int(five)
zero = int(zero)
neg_8 = int(neg_8)
T = bool(T)
F = bool(F)

print(five, type(five)) # 5 <class 'int'>
print(zero, type(zero)) # 0 <class 'int'>
print(neg_8, type(neg_8)) # -8 <class 'int'>
print(T, type(T)) # True <class 'bool'>
print(F, type(F)) # False <class 'bool'>

