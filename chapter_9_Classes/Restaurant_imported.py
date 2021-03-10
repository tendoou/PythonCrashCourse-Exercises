from Restaurant import Restaurant

new_restaurant = Restaurant('Cabana', 'sea food')

new_restaurant.open_restaurant()
new_restaurant.restaurant_description()

chinese_restaurant = Restaurant('La vaca', 'China')
chinese_restaurant.number_served = 200
chinese_restaurant.number_customers()

chinese_restaurant.set_number_serverd(300)
chinese_restaurant.number_customers()

chinese_restaurant.increment_customers(100)
chinese_restaurant.number_customers()

