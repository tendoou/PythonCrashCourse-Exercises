numbers = ['micaela', 'anita', 'estefany']
print(numbers)

message = f"My favorite number is {numbers[0]}"
print(message)
micaela = "La rubia es"
phrase = f"{micaela} {numbers[0]}"
print(phrase)

#Cambiando un valor de la lista
numbers[0] = 'shelby'
print(numbers)

#Agregando un valor a la lista (al final)
numbers.append('shelby')
print(numbers)

#Agregando un valor en una posición específica
numbers.insert(0, 'ana')
print(numbers)

#Eliminar valores de la lista
del numbers[3]
print(numbers)

#Eliminar un valor de la lista y usarlo con el método popped
ninjas = ['Sasuke', 'Naruto', 'Neji']
print(ninjas)
popped_ninjas = ninjas.pop(2)
print(ninjas)
print(popped_ninjas)
print(f"The only ninja who died in naruto was {popped_ninjas}")

#Eliminar un valor dentro de una lista
ninjas1 = ['Sasuke', 'Naruto', 'Neji']
muy_noob = 'Naruto'
ninjas1.remove(muy_noob)
print(f"{muy_noob} es muy noob")

