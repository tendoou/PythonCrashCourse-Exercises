#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])

#Eliminar un valor del diccionario.(Se removerá permanentemente).
#del alien_0['points']
#print(alien_0)

#new_points = alien_0['points']
#print(f"You just earned {new_points} points.")

#alien_0['x_position'] = 0
#alien_0['y position'] = 25
#print(alien_0)

#Empezando un diccionario vacío

#alien_0 = {}
#alien_0['color'] = 'green'
#alien_0['points'] = 5
#print(alien_0)

#Modificar valores dentro de los diccionarios

#alien_0 = {'color': 'green'}
#print(f"The alien is {alien_0['color']}")


#alien_0['color'] = 'yellow'
#print(f"The alien is now {alien_0['color']}.")

#Localizar la posición de un alien en movimiento hacia la derecha

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}.")

#mover hacia la derecha
#determinar que tan lejos se moverá según la velocidad.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.")



