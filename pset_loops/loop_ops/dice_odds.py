"""
Dice Odds
"""

Dice Odds. There are 36 possible combinations of two dice. A sim→ple pair of loops over range(6)+1 will enumerate all combinations. The sum of the two dice is more interesting than the actual combination. Create a dict of all combinations, using the sum of the two dice as the key.

Each value in the dict should be a list of tuples; each tuple has the value of two dice. The general outline is something like the following:

d= {}
Loop with d1 from 1 to 6
    Loop with d2 from 1 to 6
        newTuple ← ( d1, d2 ) # create the tuple
        oldList ← dictionary entry for sum d1+d2
        newList ← oldList + newTuple
        replace entry in dictionary with newList

Loop over all values in the dictionary
    print the key and the length of the list