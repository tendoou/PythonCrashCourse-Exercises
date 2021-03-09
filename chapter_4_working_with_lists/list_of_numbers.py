#Minimos y máximos
digits = [1, 3, 4, 5, 6]
print(min(digits))
print(max(digits))

#Expresión comprimida de un ciclo
squares = [value**3 for value in range(1, 11)]
print(squares)

#Exercises
#1.- Forma comprimida
count = [value for value in range(1, 21)]
print(count)

#2.- Forma explícita
count = []
for value in range(1, 11):
    count.append(value**3)
print(min(count))
print(max(count))
print(sum(count))

#Otra forma de asignar valores a una lista e imprimirlos asignando un saltos
new_list = list(range(3, 31, 3))
print(new_list)
