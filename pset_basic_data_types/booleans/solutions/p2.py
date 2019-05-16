"""
Booleans II - Typecasting w. Strings
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result. 

one = 1
zero = 0
bool_true = True
bool_false = False

one = str(one)
zero = str(zero)
bool_true = str(bool_true)
bool_false = str(bool_false)


print(one, type(one)) # '1' <class 'str'>
print(zero, type(zero)) # '0' <class 'str'>
print(bool_true, type(bool_true)) # 'True' <class 'str'>
print(bool_false, type(bool_false)) # 'False' <class 'str'>


# B) Use typecasting to turn the latest values for variables 'one' and 'zero' back into integers. Print the result and the datatype of the result.

one = int(one)
zero = int(zero)

print(one, type(one)) # 1 <class 'int'>
print(zero, type(zero)) # 0 <class 'int'>



# C) Use typecasting to turn the latest values for variables 'bool_true' and 'bool_false' back into boolean values. Print the result and the datatype of the result.


bool_true = bool(bool_true)
bool_false = bool(bool_false)

print(bool_true, type(bool_true)) # True <class 'bool'>
print(bool_false, type(bool_false)) # True <class 'bool'>


