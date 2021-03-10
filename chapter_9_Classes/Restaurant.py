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

