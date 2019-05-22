"""
Generate Phone Number w/Area Code
"""

# import python randomint package
from random import randint

# generate a random phone number of the form:
# 1-718-786-2825
# This should be a string
# Valid Area Codes are: 646, 718, 212
# if phone number doesn't have [646, 718, 212]
# as area code, pick one of the above at random
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
