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
        """Add the given amount to the number served."""
        self.number_served += customers


class IceCreamStand(Restaurant):
    """A simple attempt to represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'lemon', 'caramel', 'cookies']

    def display_flavors(self):
        """Display the offered ice cream flavors."""
        print(f"The {self.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


ice_cream_place = IceCreamStand('Sweetie', 'Ice cream')
ice_cream_place.display_flavors()