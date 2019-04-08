"""
Prime Numbers
"""


# check whether a number is prime
# https://www.programiz.com/python-programming/examples/prime-number


# print all primes in an interval
# https://www.programiz.com/python-programming/examples/prime-number-intervals

i = 0
primes = []

while i <= 100:
        # if i <is prime>
    primes.append(i)

print(primes)


# The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20. https://www.tutorialspoint.com/python/python_for_loop.htm

# Live Demo

for num in range(10, 20):  # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num/i  # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            break  # to move to the next number, the #first FOR
    else:                  # else part of the loop
        print(num, 'is a prime number')
