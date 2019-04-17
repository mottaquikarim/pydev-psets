"""
Sum of Squares
"""


# Write a function called "sum_squares" that finds the sum of the squares of any number of integers passed into the function.

# For example, someone could enter three individual integers, a list of five integers, or a tuple nested in a list of eight integers.

# Hint: The solution tests out different scenarios, so you can pass those numbers into your function to see if you can get the same answer for different scenarios.

def sum_squares(*nums):
  iterab = list(nums)
  
  for i in iterab:
    if isinstance(i, list) or isinstance(i, tuple):
      iterab.extend(list(i))

  squares = []

  for i in iterab:
    if not isinstance(i,int):
      continue
    elif isinstance(i,int):
      sq = i*i
      squares.append(sq)

  s = sum(squares)

  return s

a = sum_squares(4, 5, 6)
print(a)


b = sum_squares([2, 6, 3])
print(b)

c = sum_squares((3, 6, 9))
print(c)

d = sum_squares([4, 5, 6],[8, [6, 3], 2],9)
print(d)

e = sum_squares(4, ([3, 6], 8), 7)
print(e)
