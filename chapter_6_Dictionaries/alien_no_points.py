alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0)

#Usaremos el metodo 'get()' para enviar un mensaje cuando solicitemos un valor que
# no existe en nuestro diccionario

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print(alien_0.get('points')) #Imprime la palabra "none" indicando que no existe ese valor.

