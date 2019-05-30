"""
Word Frequency - SOLUTION
"""

# Print out the number of words in this movie quote. Find and print out the most common word in the quote and how many times it was used.
### Hint: You do not need a loop for this. Look up the Counter docs in python3.

from collections import Counter

princess_bride = [
'Hello', 'my', 'name', 'is', 'Inigo', 'Montoya',
'You', 'killed', 'my', 'father',
'Prepare', 'to', 'die'
]

fave_word = Counter(princess_bride)

print(fave_word.most_common(1))