"""
Phone Numbers
"""

# Parse this phone number so that a computer can process
# it. (Hint: It can't include any non-numeric
# characters.)

cell = '1.192.168.0143'
cell = cell.split('.')
cell = int(''.join(cell))

print(cell) # 11921680143