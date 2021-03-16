import random

picked_numbers = []


def guessing_number():
    print('Think in a number from 10 to 100')
    print('Enter "q" to end the program')
    print(f'Enter y/n for yes or no ')

    while len(picked_numbers) < 10:
        guess_number = random.choice(range(1, 11, 1))
        if guess_number not in picked_numbers:
            picked_numbers.append(guess_number)
            response = input(f'\nIs {guess_number} your number?:')
            if response == 'q':
                break
            if response == 'y':
                print('We won!')
                break
            else:
                if len(picked_numbers) < 10:
                    print('Ok, let me try again!')

                elif len(picked_numbers) == 10:
                    print('\nWelp, fuck you')


guessing_number()
