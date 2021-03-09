favorite_languages = {
    'jen': 'python',
    'diego': 'C',
    'areks': 'C',
    'kilito': 'SAO',
    }
#Se crea una nueva variable para hacer el comando de impresión mas limpio.
#lenguage = favorite_lenguages['diego'].title()
#print(f"Diego's favorite lenguage is {lenguage()}.")


#for name, language in favorite_languages.items(): #revisamos todos los pares de valores dentro del diccionario
   # print(f"{name.title()}'s favorite language is {language.title()}.")

#for name in favorite_languages.keys(): #revisamos solo el valor de "key"
    #print(f"\n{name.title()}")


#friends = ['jen', 'diego']
#for name in favorite_languages.keys():
    #print(f"Hi, {name.title()}")

    #if name in friends:
       # language = favorite_languages[name].title()
        #print(f"\t{name.title()}, I see you love {language}!.")

#if 'erin' not in favorite_languages.keys():
    #print("Erin, please take our poll!")

#Sortear keys para imprimir por orden alfabetico

#for name in sorted(favorite_languages.keys()):
  #  print(f"{name.title()}, thanks for taking the poll.")

#Imprimir solo los valores de un diccionario
#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
  #  print(language.title())

#Imprimir valores pero con la condición de que no se repitan
#(Esto sirve principalmente cuando quieres sacar valores de una lista muy grande

#for language in set(favorite_languages.values()):
  #  print(language.title())
#Creamos una lista de nuevas personas y revisamos si ya se encuentran dentro del diccionario
#E imprimimos un mensaje si está o no está.
new_people = ['diego', 'estefany', 'areks', 'messi', 'hazard']
for n in new_people:
    if n in favorite_languages.keys():
        print(f"\n{n.title()}, thank you for taking the poll.")

    elif n not in favorite_languages.keys():
        print(f"\n{n.title()}, can you take the poll, please? ")
