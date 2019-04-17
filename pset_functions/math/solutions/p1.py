"""
Simple Interest Calculator
"""

# Write a function called "simple_interest" that will allow a user to find out how much they will have in savings based on their current funds and an interest rate. (Instead of collecting user input, you can directly pass values of your choosing for the arguments.)

# The formula for simple interest is...
# A = P(1 + rt), where...
# P = principal amount of money
# r = interest rate
# t = number of time periods the principal will earn interest

def simple_interest(p,r,t):
  p, r, t = float(p), float(r), float(t)

  A = (p + r + t) / 100
  A = round(A,2)

  total = p + A
  total = round(total,2)

  return A, total

p = 1500
r = 2.4
t = 60

interest_accrued, total = simple_interest(p,r,t)

print(f'\nPrincipal: ${p} \nInterest Earned: ${interest_accrued} \nTotal Funds: ${total}')