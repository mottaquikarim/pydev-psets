"""
Prime Numbers I - SOLUTION
"""

# Check if a number input by a user is prime or not. If it is NOT a prime number, print out that it is not a prime number. If it IS a prime number, print out that it is a prime number and give an example of two of its factors. Hint: Prime numbers must be greater than 1.

# Example of output for a NON-prime:
# 12 is not a prime number
# For example, 2 x 6 = 12

user_input = input("Enter a number to check if it's prime: ")
num = int(user_input)

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(f'{num} is not a prime number.')
           print(f'For example, {i} x {num//i} = {num}.')
           break
   else:
       print(f'{num} is a prime number.')
else:
   print(f'{num} is a prime number.')