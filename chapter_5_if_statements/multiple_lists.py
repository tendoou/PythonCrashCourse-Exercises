#Revisar si los elementos de una lista existen en otra lista
available_toppings = ['mushrooms', 'olives', 'green pepeers', 'pepperoni',
                      'pinneaple', 'extra cheese'] #Se podria crear como un Tuple, para que no se puedan
                                                 #modificar las listas.

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("Finished making your pizza!.")
