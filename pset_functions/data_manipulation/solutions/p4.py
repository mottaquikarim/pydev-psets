"""
Rainbows & Wobniars
"""

# Write a function called "wobniar", which should contain the local variable "rainbow" below. The function should collect every other color of the rainbow starting at index 0 and add each one to a new list. When you add each color, it should be spelled backwards. For example, the word 'sing' would be added to the new list as 'gnis'. Return and print the list.

def wobniar():
  rainbow = ['red','orange','yellow','green','blue','indigo','violet']
  length = len(rainbow)  
  backwards = []

  i = 0
  while i in range(0,length+1):
    if i % 2 == 0:
      x = ''.join(reversed(rainbow[i]))
      backwards.append(x)
      i += 1
    else:
      i += 1
  
  return backwards


a = wobniar()
print(a) # ['der', 'wolley', 'eulb', 'teloiv']