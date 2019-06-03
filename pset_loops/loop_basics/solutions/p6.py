"""
GCD
"""

# Find the greatest common denominator (GCD) of two number input by a user. Then print out 'The GCD of <first number> and <second number> is <your result>.'

print('Enter two numbers to find their greatest common denominator.')

user_input1 = input('First number: ')
user_input2 = input('Second number: ')

a = int(user_input1)
b = int(user_input2)

print(f'The GCD of {a} and {b} is: ')

while b != 0:
  a, b = b, a % b

print(a)

