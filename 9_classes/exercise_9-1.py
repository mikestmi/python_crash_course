class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Intitialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a neatly formatted description of the restaurant."""
        print(f"Restaurant's {self.restaurant_name} cuisine type is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Print a statement showing the restaurant is open."""
        print(f"Restaurant {self.restaurant_name} is open.")

my_restaurant= Restaurant('Elia', 'Mediterranean')

print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
print(f"My restaurant's cuisine type is {my_restaurant.cuisine_type}.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaraunt()