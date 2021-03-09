#guardamos información en un diccionario
pizza = {'crust': "thick",
         "toppings": ['mushrooms', 'extra  cheese'],
         }
print(f"You ordered a {pizza['crust']} - crust pizza"
      f" with the following topics:")
for topping in pizza["toppings"]:
    print("\t" + topping)
