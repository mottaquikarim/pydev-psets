"""
Fibonacci Sequence
"""

# https://www.programiz.com/python-programming/examples/fibonacci-sequence

i = 0

while i <= 100:
    pass
    # add i to ... how to reference the last num...?


fibonacci = None
i = 0
fib_primes = None

for i in fibonacci:
    if i <= 50:
        # if i <is prime>
        fib_primes.append(i)
    else:
        break


# Print the first 25 numbers in the Fibonacci series and assign them to an enumerate() object called fibonacci.

# Set `fib_no` to 55, the number until where you want to print
fib_no = 55

# Set `first_no` to 0
first_no = 0

# Set `second_no` to 1
second_no = 1

# Set the counter `count` to 0
count = 0

# while loop to print the fibonacci series until the `fib_no`
while first_no <= fib_no:
    # Print `first_no`
    print(first_no)

    # Fibonnacci number
    nth = first_no + second_no

    # update values of `first_no` and `second_no`
    first_no = second_no
    second_no = nth

    # Set counter `count` +1
    count += 1


# Initialize `first_no` to `0`
first_no = 0

# Initialize `second_no` to `1`
second_no = 1

# Initialize `numbers`
numbers = '___________'

# Find and display Fibonacci series
for num in '_______':
    if(num <= 1):
        # Update only `nth`
        nth = '___'
    else:
        # Update the values `nth`, `first_no` and `second_no`
        nth = first_no + second_no
        first_no = second_no
        second_no = '__________'

    # Print `nth`
    print(nth)
