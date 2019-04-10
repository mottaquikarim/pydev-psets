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


a = ''
b = ' '
c = '  '
d = '    '
e = '        '

# for a
if len(a) == 0:
	print('True')
elif a.strip():
  print('True')
else:
	print('False')
# prints True

# ~~~~~~~~~~~~~~~~

# for b through e
if len(e) == 0:
	print('True')
elif e.strip():
  print('True')
else:
	print('False')
# prints False


# .strip() remove any spaces from a string. you do this because a string with spaces has a length and would otherwise evaluate to empty == True. But an empty string is really a falsy.