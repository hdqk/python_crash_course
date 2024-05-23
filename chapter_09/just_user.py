class User:
    """a simple model of a user"""

    def __init__(self, first_name, last_name, age, location):
        """Initializes attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """prints a summary of the user's info"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} is "
              f"{self.age} years old and lives in {self.location.title()}.")

    def greet_user(self):
        """prints a personalized greeting for the user"""
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}, "
              f"we're glad to have you back.")
