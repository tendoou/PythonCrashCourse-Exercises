prompt = "\nPlease enter three toppings for your your pizza"
prompt += "\n(Enter 'quit' if you want to cancel your order.) "
prompt += "\nToppings:"

toppings_list = ['pepperoni', 'onions', 'mushrooms', 'extra cheese']
number = 0
while True:
    topping = input(prompt)
    if topping == 'quit':
        break

    elif topping not in toppings_list:
        print("Sorry, we don't have that topping, chose another one.")
        prompt = "\nEnter another topping:"

    elif topping in toppings_list:
        number += +1
        print(f"  I'll add {topping} to your pizza.")

        if number < 3:
            prompt = "\nEnter the next topping:"
        else:
            print("\nYour order is finished, your pizza will be ready soon!")
            break
