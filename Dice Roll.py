import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(result)

        die_6 = Die()
for i in range(10):
    die_6.roll_die()

    die_10 = Die(sides=10)
for i in range(10):
    die_10.roll_die()

    die_20 = Die(sides=20)
for i in range(10):
    die_20.roll_die()