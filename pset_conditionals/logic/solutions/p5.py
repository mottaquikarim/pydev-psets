"""
truthTableEvaluator
"""

# Given the following inputs:


# P = # True or False
# Q = # True or False
# op = # '^' (logical AND, conjunction)
#      # OR, 'v' (logical OR, disjunction)
#      # OR, '->' (logical conditional, implication)
#      # OR, '<->' (biconditional)
# determine the correct outcome.

# https://medium.com/i-math/intro-to-truth-tables-boolean-algebra-73b331dd9b94

P = True
Q = True
op = '^'

if op == '^':
  if P and Q:
    print(True)
  if not P and Q:
    print(False)
  if P and not Q:
    print(False)
  if not P and not Q:
    print(False)
elif op == 'v':
  if P and Q:
    print(True)
  if not P and Q:
    print(True)
  if P and not Q:
    print(True)
  if not P and not Q:
    print(False)
elif op == '->':
  if P and Q:
    print(True)
  if not P and Q:
    print(True)
  if P and not Q:
    print(False)
  if not P and not Q:
    print(True)
elif op == '<->':
  if P and Q:
    print(True)
  if not P and Q:
    print(False)
  if P and not Q:
    print(False)
  if not P and not Q:
    print(True)
