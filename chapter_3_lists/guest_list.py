guests = ['Messi', 'Xavi', 'Iniesta']
print(f"{guests[0]}, vamos por unas cervezas")
print(f"{guests[1]}, vamos a hablar de furbol")
print(f"{guests[2]}, vamos a jugar furbol")

new_guest = 'Totti'
no_coming = 'Iniesta'
guests.remove(no_coming)
guests.insert(2, new_guest)
print(f"{no_coming} can't make it to the dinner but {new_guest} will attend in his place. This is the new guest list: \n {guests}")

popped_guest = guests.pop()
print(f"{popped_guest} can't make it to the dinner either")
guests.pop()
print(f"only {guests} is coming to the dinner")
guests.pop()
print(guests)