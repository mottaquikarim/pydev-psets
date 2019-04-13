"""
IsEmptyString
"""

# Given any empty string, of the form:

# ''
# ' '
# '  '
# # ...
# '        ' # etc
# determine if the str is empty or not (print True or False)


my_str = '    '

if my_str.strip() == '':
  print(True)
else:
  print(False)


# .strip() remove any spaces from a string. you do this because a string with spaces has a length and would otherwise evaluate to empty == True. But an empty string is really a falsy.
