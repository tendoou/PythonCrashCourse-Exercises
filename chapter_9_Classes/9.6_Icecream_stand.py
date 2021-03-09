class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def restaurant_description(self):
        print(f"{self.name} is a {self.cuisine} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def number_customers(self):
        print(f"We've served {self.number_served} customers.")

    def set_number_serverd(self, customers):
        self.number_served = customers

    def increment_customers(self, new_customers):
        self.number_served += new_customers


# Creamos la clase child
class IceStandRestaurant(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name):
        """Initialize an ice cream stand."""
        super().__init__(name, 'ice cream')
        self.flavors = []

    def display_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


jack_frost = IceStandRestaurant('Jack Frost')
jack_frost.flavors = ['Vanilla', 'Chocolate', 'Strawberry']

jack_frost.restaurant_description()
jack_frost.display_flavors()

