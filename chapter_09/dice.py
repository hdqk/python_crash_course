# Hector Delgado 5/9/2024

from random import randint


class Die:
    """simple model representing a die"""

    def __init__(self, sides=6):
        """initiates attributes of die, defaults to 6 sides"""
        self.sides = sides

    def roll_die(self, rolls=1):
        """simulates rolling a die"""
        while rolls > 0:
            print(randint(1, self.sides))
            rolls -= 1


six_sided = Die()
six_sided.roll_die(10)

ten_sided = Die(10)
ten_sided.roll_die(10)

twenty_sided = Die(20)
twenty_sided.roll_die(10)
