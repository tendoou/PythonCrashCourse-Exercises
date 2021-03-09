rivers = {'nile': 'egypt',
          'humaya': 'culiacan',
          'amazonas': 'south america',
          'titicaca': 'chile',
          }

for river, countries in rivers.items():
    print(f"The {river.title()} river runs through {countries.title()}")

print("")
print("The largest rivers in the world are:")
for river in rivers.keys():
    print(river.title())

print("\nThese are countries with large rivers:")
for country in rivers.values():
    print(country.title())
