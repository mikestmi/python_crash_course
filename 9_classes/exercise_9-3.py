class User:
    """A simple attempt to represent a user."""
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Print a neatly formatted description of the user."""
        description = f"The user {self.first_name.title()} {self.last_name.title()} is {self.age} and lives in {self.location.title()}."
        print(description)

    def greet_user(self):
        """Print a greeting to the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


user_1 = User('albert', 'einstein', '58', 'princeton')
user_1.describe_user()
user_1.greet_user()

user_2 = User('michael', 'jordan', '23', 'chicago')
user_2.describe_user()
user_2.greet_user()

user_3 = User('winston', 'churchill', '75', 'kensington')
user_3.describe_user()
user_3.greet_user()