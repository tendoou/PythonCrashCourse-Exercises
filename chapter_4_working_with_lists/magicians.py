#Correr un ciclo y asignarle cada valor de la lista a la variable e imprimir cada vuelta.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"i can't wait for the next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great show")


#Imprimir un rango de numeros y crear una lista a partir de ese rango
for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

#Seleccionar un rango de numero, indicando saltos según el múltiplo
multiplers = list(range(3, 18, 3)) #Empezaría en 3, hasta 18 , de saltos de 3
print(multiplers)

#Ejercicio de imprimir el resultado de elevar al cuadrado del 1 al 10 y asignarlos en una lista
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square) #Va agregando cada valor a la lista cada que da vuelta el ciclo
print(squares)