"""
Grades - SOLUTION
"""

# Here's a dict containing students' grades from the semester's assignments.

students = {
  'Ashton': [86, 45, 98, 100],
  'Sierra': [100, 100, 100, 100],
  'Zach': [38, 49, 90, 87],
  'Manuel': [98, 92, 86, 100],
  'Felicia': [94, 87, 89, 95],
  'Ankur': [75, 77, 77, 85],
  'Ananya': [98, 94, 87, 92],
  'Nick': [79, 84, 89, 90],
  'Olivia': [83, 91, 69, 85],
  'Molly': [83, 74, 72, 90]
}

# p 1.1) Create a dict called num_grades to store each student's average numerical grade for the semester.

num_grades = {}

for k, v in students.items():
  grade_avg = sum(v)/len(v)
  num_grades.update({k: grade_avg})

print(num_grades)

# p 1.2) Create a dict called letter_grades to store each student's final letter grade for the semester. Use A, B, C, D, and F as grades per the standard grading scale.

letter_grades = {}

for k, v in num_grades.items():
  if 100 >= v >= 90:
    letter_grades.update({k: 'A'})
  elif 90 > v >= 80:
    letter_grades.update({k: 'B'})
  elif 80 > v >= 70:
    letter_grades.update({k: 'C'})
  elif 70 > v >= 60:
    letter_grades.update({k: 'D'})
  elif 60 > v:
    letter_grades.update({k: 'F'})

print(letter_grades)

# p 1.3) Create a list of honor roll students (i.e. students who got A's).

honor_roll = []

for k, v in letter_grades.items():
  if v == 'A':
    honor_roll.append(k)

print(honor_roll)
