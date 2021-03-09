# Importamos todas las funciones del modulo Making_Pizza

import making_pizza
#Aquí específicamos qué función estamos llamando del modulo importado
making_pizza.make_pizza('personal', 'pepperoni', 'anchoys', 'extra cheese')

#Otra forma de de importar funciones específicas de x modulo.

from making_pizza import make_pizza

make_pizza('large', 'peppe')

## Le asignamos un "Alias" a la función importada en caso de que entre en conflicto con
## nuestro código actual

from making_pizza import make_pizza as mp
mp('large', 'peppe')

## Tambien se le puede crear un alias a los módulos

import making_pizza as ma_pi

ma_pi.make_pizza('large', 'onions')
