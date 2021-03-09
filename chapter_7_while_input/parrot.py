prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? " #continuamos con el mismo mensaje pero en otra linea
name = input(prompt)
print(f"\nHello, {name}!")


age = input("How old are you? ")
age = int(age) #Al recibir un número, será string y necesitamos decirle a python que lo use como int
if age >= 18:
    print("\nYou're old enough to vote, make a good choice!")