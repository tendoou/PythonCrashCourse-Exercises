import random


def guessing_number():
    print('Think in a number from 10 to 100')
    print('Enter "q" to end the program')
    print(f'Enter y/n for yes or no ')

    number_trials = 0

    while number_trials < 10:
        guess_number = random.choice(range(1, 101, 1))

        response = input(f'\nIs {guess_number} your number?:')
        if response == 'q':
            break
        if response == 'y':
            print('We won!')
            break
        else:
            number_trials += 1
            if number_trials < 9:
                print('Ok, let me try again!')

            elif number_trials == 10:
                print('\nWelp, fuck you')


guessing_number()