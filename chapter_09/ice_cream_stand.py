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


class IceCreamStand(Restaurant):
    """simple model of an ice cream stand"""

    def __init__(self, name, cuisine):
        """Initialize the parent attributes and others"""
        super().__init__(name, cuisine)
        self.flavors = ['strawberry', 'chocolate', 'vanilla']

    def display_flavors(self):
        """prints a list of ice cream flavors"""
        print("Here are the flavors of ice cream we have:")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_store = IceCreamStand('sub zero', 'ice cream')
my_store.display_flavors()
