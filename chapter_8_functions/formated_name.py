#def get_formatted_name(first_name, last_name):
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)


## Agregamos una opción en caso de que se proporcione un segundo nombre

def get_middle_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name1 = f"{first_name} {middle_name} {last_name}"
    else:
        full_name1 = f"{first_name} {last_name}"

    return full_name1.title()

musician1 = get_middle_name('jimi', 'hendrix')
print(musician1)
#El orden de los input tienen que ser como lo indica la función (middle name al final porque es opcional)
musician1 = get_middle_name('jimi', 'hendrix', 'lee')
print(musician1)