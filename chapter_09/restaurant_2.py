class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize the name nad cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.name.title()} serves {self.cuisine.title()} food.")

    def open_restaurant(self):
        """Prints a message saying the restaurant is open."""
        print(f"{self.name.title()} is open for business!")


restaurant = Restaurant('lucky duck', 'chinese')

print(f"{restaurant.name}")
print(f"{restaurant.cuisine}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
