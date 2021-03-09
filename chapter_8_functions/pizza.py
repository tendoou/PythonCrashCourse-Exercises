def make_pizza(*toppings):
##"""Print the list of toppings that have been requested."""
    print(toppings)

## Agregamos un ciclo para imprimir en orden los ingredientes.
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

##Funcion mezclando tipos de parámetros (fijos y arbitrarios) El arbitrario siempre tiene que ir al final.

def make_pizza(size, *toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('medium', 'pepperoni')
make_pizza('familiar', 'mushrooms', 'green peppers', 'extra cheese')
