"""
Word Frequency - SOLUTION
"""

from collections import Counter

princess_bride = [
'Hello', 'my', 'name', 'is', 'Inigo', 'Montoya',
'You', 'killed', 'my', 'father',
'Prepare', 'to', 'die'
]

fave_word = Counter(princess_bride)

print(fave_word.most_common(1))