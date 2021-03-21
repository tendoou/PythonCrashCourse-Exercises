from Password_Manager import PasswordManager


def action_menu(entry):
    while True:

        print('\n1. Register new login info')
        print('2. Consult login info')
        print('3. Delete login info')
        print('4. End the program.')
        action = input('What do you want to do?:')
        if action == '1':
            ws = input('ws')
            us = input('us')
            p = input('p')
            entry.register_login_info(ws, us, p)
        if action == '2':
            credential = entry.consult_login_info()
        if action == '3':
            entry.delete_login_info()
        if action == '4':
            break


entry1 = PasswordManager()
action_menu(entry1)


