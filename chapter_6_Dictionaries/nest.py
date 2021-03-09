#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}
#aliens = [alien_0, alien_1, alien_2] #Creamos una lista con los diccionarios

#Crearemos una flota de 30 aliens
#Creamos una lista vacía para almacenar aliens
aliens = []

#Make 30 green alines
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)

#modificar el color de los 3 primeros aliens
for alien in aliens[10:20]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[21:30]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

#Show the first 5 aliens.
for alien in aliens[:30]:
    print(alien)

#Show the total number of aliens
print(f"Total number of aliens is: {len(aliens)}")