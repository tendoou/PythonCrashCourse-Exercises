#Sortear una lista alfabeticamente en ambos sentidos permanentemente
cars = ['bmw', 'audi', 'honda']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#Sortear una lista de manera temporal en ambos sentidos
colors = ['blue', 'red', 'black', 'purple', 'yellow', 'pink']
print(colors)
print(sorted(colors))
print(colors)

#Sortear una lista en orden inverso al que se capturó
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)
print(len(numbers)) #Calculando la longitud de una lista

