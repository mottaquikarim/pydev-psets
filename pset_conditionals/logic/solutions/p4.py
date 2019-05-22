"""
Empty Strings
"""

# Given any empty string, of the form:

# ''
# ' '
# '  '
# any other num of spaces...

# determine if the str is empty or not (print True or False). Hint: You'll need to look up how to remove trailing spaces from a string.


my_str = '    '

if my_str.strip() == '':
  print(True)
else:
  print(False)


# .strip() removes any spaces from a string. you do this because a string with spaces has a length and would otherwise evaluate to empty == True. But an empty string is really a falsy.
