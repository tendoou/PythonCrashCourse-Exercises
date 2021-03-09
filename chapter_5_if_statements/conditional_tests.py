pet = 'dog'
new_pet = 'DoG'
print(pet == 'cat')
print(pet != 'cat')

print(pet == new_pet)
print(pet.lower() == new_pet.lower())

criminals = ['manson', 'kilito', 'el chapo']
user = 'el chapo'
if user in criminals:
    print("no puede pasar")
else:
    print("adelante caballero")
#Comparativa rapida si queremos saber si un elemento se encuentra dentro de una lista.
print(user in criminals)

#IF, elife y else
age = 70
if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65: #Se puede usar elife en lugar de else para ser más precisos en todas las instrucciones del programa
    price = 20
print(f"Your admission cost is ${price}.")
