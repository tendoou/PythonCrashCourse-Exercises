pets = ['dog', 'cat', 'parrot', 'cat', 'cat', 'dog', 'rabbit']
print(pets)

while 'cat' in pets: #Ciclamos para ir removiendo el valor 'cat' de la lista.
    pets.remove('cat')
print(pets)