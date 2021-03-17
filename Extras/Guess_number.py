import random
import numpy
picked_numbers = []


def get_options(banned_numbers, a, b):
    options = []

    for option in range(a, b):
        if option not in banned_numbers:
            options.append(option)
    return options


tried_numbers = []


def smart_guess_number():
    print('Enter "q" to end the program')
    print('Set a range of numbers')
    a = input('First number:')
    a = int(a)
    b = input('Second number:')
    b = int(b)
    trials = 0
    while trials < 10:
        options = get_options(tried_numbers, a, b)
        guessing = (round(numpy.median(options)))
        tried_numbers.append(guessing)

        response = input(f'Is {guessing} your number?(type y/n):')
        if response == 'y':
            print('I won!')
            break
        if response == 'q':
            break
        else:
            trials += 1
            more_less = input(f'Mm, L<{guessing}<G?:(type l/g):')
            if more_less == 'l':
                b = guessing
            else:
                a = guessing

            if trials < 9:
                print("Ok, i'll try again")
            elif trials == 10:
                print('Ok, i lost')


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


smart_guess_number()
