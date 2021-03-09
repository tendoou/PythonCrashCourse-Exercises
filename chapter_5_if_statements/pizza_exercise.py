requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Ciclos con if

for requested_topping in requested_toppings:
    if requested_topping == 'extra cheese':
        print("Sorry, we're out of extra cheese right now.")
    else:
        print(f"Adding {requested_topping}.")

#Revisar si una lista está vacia
requested_toppings = []
if requested_toppings: #Verificamos si la lista contiene elementos para entrar al ciclo, si no tiene, pasaremos al else
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}.")
        print("\nFinishing your pizza.")
else:
    print("\nAre you sure you want a plain pizza?")
