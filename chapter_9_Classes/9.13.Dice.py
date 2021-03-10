from random import randint


class Dice:
    """Represents a dice, that can be rolled"""
    def __init__(self, sides=6):
        self.sides = sides

    """Return a number between 1 and the number of dice's sides"""
    def roll_dice(self):
        return randint(1, self.sides)


# Make a 6-sided dice, and show 10 results
d6 = Dice()

results = []

for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 Rolls of a 6-sided dice:")
print(results)


d10 = Dice(10)

results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("\n10 Rolls of a 10-sided dice:")
print(results)
