"""
Typecasting Booleans I
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result. 

one = 1
zero = 0

one = bool(one)
zero = bool(zero)

print(one, type(one)) # True <class 'bool'>
print(zero, type(zero)) # False <class 'bool'>

# B) Use typecasting to turn the resultant variables from part A into floats. Print the result and the datatype of the result.

one = float(one)
zero = float(zero)

print(one, type(one)) # 1.0 <class 'float'>
print(zero, type(zero)) # 0.0 <class 'float'>


# C) Use typecasting to turn the resultant variables from part B back into booleans. Print the result and the datatype of the result.

one = bool(one)
zero = bool(zero)

print(one, type(one)) # True <class 'bool'>
print(zero, type(zero)) # False <class 'bool'>

# D) Use typecasting to turn the resultant variables from part C into integers. Print the result and the datatype of the result.

one = int(one)
zero = int(zero)

print(one, type(one)) # 1 <class 'int'>
print(zero, type(zero)) # 0 <class 'int'>


# E) Use typecasting to turn the variable below into a boolean value. Print the result and the datatype of the result. 

ten = 10

ten = bool(ten)

print(one, type(one)) # True <class 'bool'>
