"""
Typecasting Booleans II
"""

# A) Use typecasting to turn these variables into strings. Print the result and the datatype of the result. 

one = 1
zero = 0
T = True
F = False

one = str(one)
zero = str(zero)
T = str(T)
F = str(F)


print(one, type(one)) # '1' <class 'str'>
print(zero, type(zero)) # '0' <class 'str'>
print(T, type(T)) # 'True' <class 'str'>
print(F, type(F)) # 'False' <class 'str'>


# B) Use typecasting to turn the latest values for variables 'one' and 'zero' back into integers. Print the result and the datatype of the result.

one = int(one)
zero = int(zero)

print(one, type(one)) # 1 <class 'int'>
print(zero, type(zero)) # 0 <class 'int'>



# C) Use typecasting to turn the latest values for variables 'T' and 'F' back into boolean values. Print the result and the datatype of the result.

T = bool(T)
F = bool(F)

print(T, type(T)) # True <class 'bool'>
print(F, type(F)) # True <class 'bool'>

