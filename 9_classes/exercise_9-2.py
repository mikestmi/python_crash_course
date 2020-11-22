class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Intitialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a neatly formatted description of the restaurant"""
        print(f"Restaurant's {self.restaurant_name} cuisine type is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Print a statement showing the restaurant is open."""
        print(f"Restaurant {self.restaurant_name} is open.")

restaurant_1 = Restaurant('Elia', 'Mediterranean')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Mirch', 'Indian')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Nolan', 'Asian')
restaurant_3.describe_restaurant()