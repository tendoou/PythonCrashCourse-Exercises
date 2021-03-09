current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: #Esta condicion dice que si un numero es divisible entre 2
        continue                #Ignore el resto del programa y vuelva a empezar el ciclo.
    print(current_number)       #Por eso no se imprime el valor del 2.