"""
Password Requirements
"""

# Write a Python program called "pw_validator" to validate a password based on the security requirements outlined below.

# VALIDATION REQUIREMENTS:
## At least 1 lowercase letter [a-z]
## At least 1 uppercase letter [A-Z].
## At least 1 number [0-9].
## At least 1 special character [~!@#$%&*].
## Min length 6 characters.
## Max length 16 characters.

def pw_validator(pw):
  pw = list(pw)

  if len(pw) < 6 or len(pw) > 16:
    return 'Please enter a valid password.'

  num_count = 0
  lower_count = 0
  upper_count = 0
  spec_count = 0

  for i in pw:
    # check numbers
    if i in '0123456789':
      idx = pw.index(i)
      pw[idx] = int(i)
      num_count += 1
    # check lowercase letters
    if i in 'abcdefghijklmnopqrstuvwxyz':
      idx = pw.index(i)
      lower_count += 1
    # check uppercase letters
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      idx = pw.index(i)
      upper_count += 1
    # check special char
    if i in '~!@#$%&*':
      idx = pw.index(i)
      spec_count += 1

  if num_count == 0 or lower_count == 0 or upper_count == 0 or spec_count == 0:
    return 'Please enter a valid password.'
  else: 
    return 'Success!'

# < 6 char
a = pw_validator('abc')
print(f'abc: {a}')

# > 16 char
b = pw_validator('1234567890abcdefg')
print(f'1234567890abcdefg: {b}')

# no numbers
c = pw_validator('@bcdEFGh!j')
print(f'@bcdEFGh!j: {c}')

# no lowercase letters
d = pw_validator('@BCD3EFGH!J')
print(f'@BCD3EFGH!J: {d}')

# no uppercase letters
e = pw_validator('@bcd3efgh!j')
print(f'@bcd3efgh!j: {e}')

# no special characters
f = pw_validator('Abcd3FGhIj112')
print(f'Abcd3FGhIj112: {f}')

# valid pw
g = pw_validator('P$kj35S&7')
print(f'P$kj35S&7: {g}')