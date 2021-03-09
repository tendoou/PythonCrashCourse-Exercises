favorite_places = {
                   'diego': ['europe', 'canada', 'usa'],
                   'estefany': ['ecuador', 'new york'],
                   'mama': ['cancun'],
                    }
for name, places in favorite_places.items():
    print(f"\nThe favorite places for {name.title()} are:")
    for place in places:
        print(f"\t{place.title()}")
#Se usa un nuevo ciclo para imprimir todos los valores que contiene cada key.