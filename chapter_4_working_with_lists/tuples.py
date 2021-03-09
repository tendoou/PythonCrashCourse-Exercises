#TUPLES : Listas que no se van a modificar durante un programa
dimensions = (200, 50)
print(dimensions)

#Redefinir el contenido de la tuple
dimensions = (300, 40)
print(dimensions)

#ejercicio
menu = ('pasta', 'pizza', 'hamburger', 'fries', 'ice cream')

menu = ('sandwich', 'panini', 'hamburger', 'fries', 'ice cream')
print("The new menu is:")
for meals in menu:
    print(meals)
