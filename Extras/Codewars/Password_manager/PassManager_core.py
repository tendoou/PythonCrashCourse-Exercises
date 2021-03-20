from Password_Manager import PasswordManager

print('Menu of actions:')
print('1. Consult login info')
print('2. Register new login info')
print('3. Delete login info')
action = input('What do you want to do?:')


def action_menu():
    if action == '1':
        consult_login_info()
    if action == '2':
        PasswordManager.register_login_info()
    if action == '3':
        delete_login_info()


def consult_login_info():
    pass





def delete_login_info():
    pass

