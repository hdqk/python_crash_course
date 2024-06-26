from random import randint


class Die:
    """A class representing a single 6-sided die."""

    def __init__(self, num_sided=6):
        """Assume a six-sided die."""
        self.num_sides = num_sided

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)
