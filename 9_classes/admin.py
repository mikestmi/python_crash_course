from user import User

class Privileges:
    """A simple attempt to represent administator's privileges."""

    def __init__(self):
        """Intitialize privileges attributes."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the administrator's privileges."""
        print(f"The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


class Admin(User):
    """A simple attempt to represent an administator."""

    def __init__(self, first_name, last_name, age, location):
        """Intitialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
