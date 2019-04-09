"""
Factorial - SOLUTION
"""

# Find the factorial of a number input by a user. Then print out the factors within the factorial and then print out the actual numeric answer. Hint: The formula for a factorial is n! = (n-1)*n.

# Example output:
"""
8! = 8*7*6*5*4*3*2*1
8! = 40320
"""

print('Enter a number to find its factorial: ')
initial = input()
num = int(initial)

fac = []

while num >= 1:
  fac.append(num)
  num -= 1

factorial = f'{initial}! = '
product = 1

for index, value in enumerate(fac):
  if value > 1:
    factorial = factorial+str(value)+'*'
    product = product*value
  elif value == 1:
    factorial = factorial+str(value)

print(factorial+'\n8! =', product)