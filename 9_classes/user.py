class User:
    """A simple attempt to represent a user."""

    def __init__(self, first_name, last_name, age, location):
        """Intitialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a neatly formatted description of the user."""
        description = f"The user {self.first_name.title()} {self.last_name.title()} is {self.age} and lives in {self.location.title()}."
        print(description)

    def greet_user(self):
        """Print a greeting to the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login attempts to 0."""
        self.login_attempts=0
