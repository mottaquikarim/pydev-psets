"""
String Operators
"""

# Create two variables, each of which is half of a compound sentence. Do NOT add any punctuation up front. Add the two variables together, and print the result.
## Example compound sentence: "I'll go to the beach today and I'll go snorkeling" 


## ADDING STRINGS (Okay)
var1 = 'I\'ve been to India '
var2 = 'and I got to see the Taj Mahal'

var3 = print(var1 + var2)


## STRING FORMATTING (BETTER!)
var1 = 'I\'ve been to India'
var2 = 'and I got to see the Taj Mahal'

var3 = print(f'{var1}, {var2}!')

# Notice something here? String formatting gives you more flexibility to customize values dynamically.