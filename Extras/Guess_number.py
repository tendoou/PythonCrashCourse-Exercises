import random

picked_numbers = []


def get_options(banned_numbers):
    options = []

    for option in range(1, 11):
        if option not in banned_numbers:
            options.append(option)
    return options


def smart_guess_number():
    print('Enter "q" to end the program')
    print('Set a range of numbers')
    a = input('First number:')
    a = int(a)
    b = input('Second number:')
    b = int(b)
    if b % 2 == 0:
        guessing = b/2
    else:
        guessing = b / 2 + 1
    guessing = (b / 2) + 1
    print(guessing)
    print(f'Enter y/n for yes or no ')


def guessing_number():
    print('Think in a number from 10 to 100')
    print('Enter "q" to end the program')
    print(f'Enter y/n for yes or no ')

    while len(picked_numbers) < 10:
        options = get_options(picked_numbers)
        guess_number = random.choice(options)
        picked_numbers.append(guess_number)
        response = input(f'\nIs {guess_number} your number?:')

        if response == 'q':
            break
        if response == 'y':
            print('I won!')
            break
        else:
            if len(picked_numbers) < 10:
                print('Ok, let me try again!')
            elif len(picked_numbers) == 10:
                print('\nWelp, fuck you')


guessing_number()
