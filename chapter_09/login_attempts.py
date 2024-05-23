class User:
    """a simple model of a user"""

    def __init__(self, first_name, last_name, age, location, login_attempts):
        """Initializes attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """prints a summary of the user's info"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} is "
              f"{self.age} years old and lives in {self.location.title()}.")

    def greet_user(self):
        """prints a personalized greeting for the user"""
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}, "
              f"we're glad to have you back.")

    def increment_login_attempts(self):
        """increments login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets loging attempts to zero"""
        self.login_attempts = 0


user1 = User('hector', 'delgado', '35', 'santo domingo', 0)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.reset_login_attempts()
print(f"{user1.login_attempts}")
