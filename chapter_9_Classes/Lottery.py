from random import choice
import string

possibilities = []
winner_ticket = []


# We set the range of possibilities of numbers and letters to pull.
def set_possibilities(number, letter):
    if letter not in list(string.ascii_uppercase) or type(number) != int:
        raise ValueError("Error, we only accept numbers and uppercase letters.")

    for nums in range(0, number):
        possibilities.append(nums)

    for c in list(string.ascii_uppercase)[:ord(letter)]:
        possibilities.append(c)
    print("Items are set successfully")


def announce_winner_ticket():

    if possibilities:
        while len(winner_ticket) < 5:
            pulled_item = choice(possibilities)

            if pulled_item not in winner_ticket:
                print(f"We pulled a: {pulled_item}!")
                winner_ticket.append(str(pulled_item))

        print(f"\nThe winner ticket is: \n{'-'.join(winner_ticket)}")

    else:
        print("Error, you need to set up items first.")


set_possibilities(9, 'F')
announce_winner_ticket()
