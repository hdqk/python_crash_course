# Hector Delgado 5/16/2024

class Employee:
    """"""

    def __init__(self, first, last, salary):
        """Initializes attributes"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        """Gives a raise to the salary, default is 5000"""
        self.salary += increase
