class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize the name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.name.title()} serves {self.cuisine.title()} food.")

    def open_restaurant(self):
        """Prints a message saying the restaurant is open."""
        print(f"{self.name.title()} is open for business!")


r1 = Restaurant('lucky duck', 'chinese')
r1.describe_restaurant()

r2 = Restaurant('slippery noodle', 'italian')
r2.describe_restaurant()

r3 = Restaurant('los tres golpes', 'dominican')
r3.describe_restaurant()
