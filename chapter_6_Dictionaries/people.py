diego = {
         'name': 'diego',
         'gender': 'male',
         'age': 29,
         'country': 'Mexico',
         'ocupation': 'civil engineer'
         }

areks = {
         'name': 'areks',
         'gender': 'male',
         'age': 29,
         'country': 'Mexico',
         'ocupation': 'programmer',
         }

estefany = {
         'name': 'estefany',
         'gender': 'female',
         'age': 27,
         'country': 'ecuador',
         'ocupation': 'student',
         }
people = [diego, areks, estefany]

for data in people:
    name = data['name'].title()
    age = data['age']
    country = data['country'].title()
    ocupation = data['ocupation'].title()
    gender = data['gender']

    if gender == 'male':
        print(f"{name} is {age}, he's from {country} and his ocupation is {ocupation}.")

    elif gender == 'female':
        print(f"{name} is {age}, she's from {country} and her ocupation is {ocupation}.")

    else:
        print(f"{gender} is not a gender idiot.")
