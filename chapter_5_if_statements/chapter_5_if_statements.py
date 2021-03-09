#Ejercicios con condiciones, poner siglas en mayusculas y nombres con solo la letra inicial
cars = ['subaru', 'toyota', 'bmw', 'nissan']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Multiples condiciones "and" y "or"
age_0 = 18
age_1 = 21
if age_0 >= 21 and age_1 >= 21:
    print("true")


#Se puede crear el booleano directamente dentro del print
if age_0 >= 21 or age_1 >= 21:
    print(age_0 >= 21 or age_1 >= 21)

#Revisar si un valor está dentro de una lista
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print("true")

#si no está
banned_users= ['diego', 'pepe', 'miguel']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
