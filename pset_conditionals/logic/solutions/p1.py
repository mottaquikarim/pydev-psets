"""
Calculate Grade
"""

# write a program that will print the "letter"
# equivalent of the grade, for example:
# when grade = 90 # -> expect A
# when grade = 80 # -> expect B
# when grade = 70 # -> expect C
# when grade = 60 # -> expect D
# when grade = 54 # -> expect F
# when grade = -10 # -> expect Error
# when grade = 10000 # -> expect Error
# when grade = "lol skool sucks" # -> expect Error

grade = 15  # expect this to be a number

if 100 >= grade >= 90:
    print('A')
elif 89 >= grade >= 80:
    print('B')
elif 79 >= grade >= 70:
    print('C')
elif 69 >= grade >= 60:
    print('D')
elif 59 >= grade >= 0:
    print('F')
else:
    print('Error')