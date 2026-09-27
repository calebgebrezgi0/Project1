import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

die_6 = Die()
results_6 = []
for i in range(10):
    results_6.append(die_6.roll_die())
print("10 rolls of a 6-sided die:")
print(results_6)

die_10 = Die(sides=10)
results_10 = []
for i in range(10):
    results_10.append(die_10.roll_die())
print("\n10 rolls of a 10-sided die:")
print(results_10)

die_20 = Die(sides=20)
results_20 = []
for i in range(10):
    results_20.append(die_20.roll_die())
print("\n20 rolls of a 20-sided die:")
print(results_20)