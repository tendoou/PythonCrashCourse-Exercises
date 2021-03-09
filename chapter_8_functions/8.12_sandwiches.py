def making_sandwich(*toppings):
    print("Making your sandwich withe the following ingredients:\t")
    for topping in toppings:
        print(f"{topping}")

making_sandwich('ham', 'tomato', 'chips', 'aguacate')