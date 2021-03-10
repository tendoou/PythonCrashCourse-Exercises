import random

class Die:
    """Represents a die, who can be rolled"""
    def __init__(self, sides=6):
        self.sides = sides

    """Return a number between 1 and the number of die's sides"""
    def roll_die(self):
        randit(1, self.sides)

#Make a 6-sided die, and show 10 results

d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 Rolls of a 6-sided die:")
print(results)


d10 = Die()

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 Rolls of a 10-sided die:")
print(results)