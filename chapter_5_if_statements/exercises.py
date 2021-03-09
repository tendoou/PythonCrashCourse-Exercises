#Ejercicios con condicionales
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

ages = [21, 17, 25, 18, 15, 20, 20]
persons = 0
for age in ages:
    if age < 21:
        persons = persons + 1
print(f"{persons} personas no cumplen con la edad mínima.")

