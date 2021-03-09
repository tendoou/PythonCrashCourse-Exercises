prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit': #Agregamos esta condición para que no imprima la palabra 'quit'
        print(message)    #y solo termine de correr el programa.
