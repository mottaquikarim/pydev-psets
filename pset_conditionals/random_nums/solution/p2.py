"""
Generate Phone Number w/Area Code
"""

# Generate a random phone number using these SPECS:
### Should be a string in this format: 1-718-786-2825
### Must randomly choose one of these area codes: 646, 718, 212

from random import randint

areacode = randint(1, 3)

str_ = "1-"
if areacode == 1:
    str_ += "718"
if areacode == 2:
    str_ += "646"
if areacode == 3:
    str_ += "212"

str_ += f"-{randint(100,999)}-{randint(1000,9999)}"

print(str_)
