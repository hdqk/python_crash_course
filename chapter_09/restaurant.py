"""A class that can be used to represent a restaurant."""


class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize the name nad cuisine attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.name.title()} serves {self.cuisine.title()} food "
              f"and has served {self.number_served} customers.")

    def open_restaurant(self):
        """Prints a message saying the restaurant is open."""
        print(f"{self.name.title()} is open for business!")

    def set_number_served(self, set_served):
        """set the number of customer's served to new value"""
        self.number_served = set_served

    def increment_number_served(self, served):
        """increments the number of customers served"""
        if served >= 0:
            self.number_served += served
        else:
            print("Invalid entry: customers served must be a positive number.")
