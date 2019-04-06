# import io
# import pytest

# from unittest import TestCase
# from unittest.mock import patch


# SOLUTION

princess_bride = [
'Hello', 'my', 'name', 'is', 'Inigo', 'Montoya',
'You', 'killed', 'my', 'father',
'Prepare', 'to', 'die'
]


# must be a more succinct way to do this

print(len(princess_bride))
word_counts = None

for i in princess_bride:
	instances = princess_bride.count(i)
	word_counts.update(i,instances)

sorted(instances)
print()