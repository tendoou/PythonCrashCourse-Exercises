#Tomando ciertos valores dentro de una lista
players = ['Diego', 'Messi', 'Xavi', 'Iniesta', 'Pedro']
print(players[0: 3])

#Lopping through a Slice

for player in players[:3]:
    print(player.title())

#Copiar el contenido de una lista en otra independiente
my_foods = ['Pizza', 'Hamburguesa', 'Tacos']
friend_foods = my_foods[:]
my_foods.append('Ice cream')
friend_foods.append('Mariscos')
print("\nMy favorite dishes are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite dishes are:")
for friend_food in friend_foods:
    print(friend_food)



#Ejercicios
objetos = ['carro', 'moto', 'barco', 'avion',' helicoptero']
print(f"The first 3 items in the list are: {objetos[0:3]}")
print(f"The 3 items in the middle of the list are: {objetos[1:4]}")
print(f"The last 3 items of the list are: {objetos[2:5]}")
