sandwich_orders = ['salami', 'jam', 'chicken', 'pastrami', 'turkey', 'tuna','pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("Sorry, we're out of pastrami today.") #Eliminamos un ingrediente que no tenemos
while 'pastrami' in sandwich_orders:         #antes de que se añada a nuestra lista vacía.
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:

    making_sandwiches = sandwich_orders.pop()
    print(f"I made your {making_sandwiches} sadwich.")
    finished_sandwiches.append(making_sandwiches.title())

print("\nThe next sandwiches are finished:")
for sandwiches in finished_sandwiches:
    print(f"\t{sandwiches} sandwich.")

