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

new_restaurant =Restaurant('Cabana', 'sea food')

new_restaurant.open_restaurant()
new_restaurant.restaurant_description()

chinese_restaurant = Restaurant('La vaca', 'China')
chinese_restaurant.number_served = 200
chinese_restaurant.number_customers()

chinese_restaurant.set_number_serverd(300)
chinese_restaurant.number_customers()

chinese_restaurant.increment_customers(100)
chinese_restaurant.number_customers()