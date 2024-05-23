from just_user import User


class Admin(User):
    """a simple model of an admin-level user"""

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        """Initializes attributes"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """prints a list of user privileges"""
        print(f"These are the current user's privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
