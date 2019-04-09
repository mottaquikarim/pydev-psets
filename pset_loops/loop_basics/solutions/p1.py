"""
Odds & Evens - SOLUTION
"""

# Use a loop to make a list of all odd numbers between 1 and 10 and another list with all the evens. When done, print the lists.

odds = []
evens = []

i = 1

while i <= 10:
  if i % 2 != 0:
    odds.append(i)
  else:
    evens.append(i)
  i += 1

print(odds,'\n', evens)