from Password_Manager import PasswordManager


def action_menu(entry):
    while True:

        print('\n1. Register new login info')
        print('2. Consult login info')
        print('3. Delete login info')
        print('4. End the program.')
        action = input('What do you want to do?:')
        if action == '1':
            ws = input('Website:')
            us = input('Username:')
            p = input('Password:')
            if entry.register_login_info(ws, us, p):
                print('Your login info has been saved successfully.')
            else:
                print('The website does not exist')
        if action == '2':
            consult = input('Which website do you want to consult?:')
            credential = entry.consult_login_info(consult)
            print(f'This is your info:{credential.__dict__}')
        if action == '3':
            delete = input('Type the website to delete:')
            response = input(f'Are you sure you want to delete the {delete} register? (y/n):')
            if response == 'y':
                entry.delete_login_info(delete)
                print(f'The entry has been deleted.')

        if action == '4':
            break


entry1 = PasswordManager()
action_menu(entry1)


