"""
Play RPS w/Bad Input
"""

p1 = None  # can be invalid!
p2 = None  # can be invalid!

"""
This is the same as the original RPS problem, 
except that cannot expect the input to be valid. 
While we *want* `r` or `p` or `s`, there is a possibility 
that input can be anything like...

* `ROCK` (all caps)
* `R` (`r` but capitalized)
* `PAPrrRR` (incorrectly spelled, upper/lowercased)

Implement conditional statements that will sanitize the 
user input or let user know that input is invalid.
"""
