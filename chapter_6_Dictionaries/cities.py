cities = {
          'olkahoma': {
              'country': 'usa',
              'population': 649021,
              'franchise': 'okc thunder'
          },

          'houston':
              {'country': 'usa',
               'population': 2326000,
               'franchise': 'rockets'
               },

          'los angeles':
              {"country": 'usa',
               'population': 12447000,
               'franchise': 'lakers'
               },
        }
#Ciclamos para asignar el valor de key a una variable temporal y creamos 3 variables para value
#ya que posee 3 datos dentro.
for city, city_info in cities.items():
    country = city_info['country'].upper()
    population = city_info['population']
    franchise = city_info['franchise'].title()

    print(f"\n{city} is in {country}.")
    print(f"It has a population of {population}.")
    print(f"His main NBA franchise is {franchise}.")

