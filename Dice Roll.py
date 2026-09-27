import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(result)