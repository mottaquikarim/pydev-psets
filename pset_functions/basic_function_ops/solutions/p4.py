"""
Function Basics IV - Multiple Return Values
"""

# Write a and call a function called "figures" that takes any two numbers and **individually** returns the following as integers:
# their sum
# their product
# the quotient for num1 / num2

"""Print each value out individually in this format:
(using 12 and 3)
sum: 15
product: 36
quotient: 4
"""

def figures(num1,num2):  
  # sum
  s = int(num1 + num2)

  # product
  p = int(num1 * num2)

  # quotient
  q = int(num1 / num2)

  return s, p, q


x = figures(21.689,8.123)
s, p, q = x
print(f"""
sum: {s}
product: {p}
quotient: {q}
""")

"""
sum: 29
product: 176
quotient: 2
"""

