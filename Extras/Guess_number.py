import random


def guessing_number():
    print('Enter "q" to end the program')
    number = input('Give me a number in between 10 and 100:')
    print(f'Enter y/n for yes or no ')

    number_trials = 0

    while number_trials < 10:
        guess_number = random.choice(range(1, int(number), 1))

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

        print('Welp, fuck you')

guessing_number()