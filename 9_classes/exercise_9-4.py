class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Intitialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a neatly formatted description of the restaurant."""
        print(f"Restaurant's {self.restaurant_name} cuisine type is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Print a statement showing the restaurant is open."""
        print(f"Restaurant {self.restaurant_name} is open.")

    def set_number_served(self, served_customers):
        """Set the number of the served customers."""
        self.number_served = served_customers

    def increment_number_served(self, customers):
        """Add the given amount to the number served"""
        self.number_served += customers


my_restaurant= Restaurant('Elia', 'Mediterranean')
print(f"The number of customers the restaurant has served is {my_restaurant.number_served}.")

my_restaurant.number_served = 7
print(f"The number of customers the restaurant has served is {my_restaurant.number_served}.")

my_restaurant.set_number_served(23)
print(f"The number of customers the restaurant has served is {my_restaurant.number_served}.")

my_restaurant.increment_number_served(14)
print(f"The number of customers the restaurant has served is {my_restaurant.number_served}.")