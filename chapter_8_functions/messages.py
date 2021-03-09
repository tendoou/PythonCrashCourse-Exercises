#def print_messages(messages):
    #for message in messages:
        #print(message)

#Se le puede poner el nombre que quiera a la lista mientras coincida a la hora de llamar a la función
#phrases = ['hola wey', 'que tal estas', 'hai hai']
#print_messages(phrases)

def send_messages(messages, sent_messages):
    print("We have to send these messages:")
    while messages:
        new_messages = messages.pop()
        print(new_messages)
        sent_messages.append(new_messages)


messages_1 = ['holi', 'que pasa', 'chaval']
sent_messages = []

send_messages(messages_1[:], sent_messages) ##Lllamamos a una copia de la lista para conservar la original intacta.

print("\nFinal list:")
print(messages_1)
print(sent_messages)
