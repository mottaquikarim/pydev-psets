"""
Factors
"""

# Find all factors of a number that a user inputs and print out 'The factors of <the_user_input_number> are: '.

# user_input = input("Enter a number to find its factors: ")

grades = [100, 98, 76, 54, 98, 89]
curved_grades = []

for grade in grades:
  curved_grades.append(grade + 10)

print(curved_grades)

curved_grades2 = [(grade + 10) for grade in grades]
curved_grades3 = map(grades, lambda g: g + 10)

who_failed = []
for grade in grades:
  if grade < 65:
    who_failed.append(grade)
  
print(who_failed)

who_failed = [grade for grade in grades if grade < 65]