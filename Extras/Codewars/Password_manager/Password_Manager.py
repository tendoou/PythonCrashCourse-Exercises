import json
class PasswordManager:
    def __init__(self, credentials=[]):
        self.credentials = credentials

    def register_login_info(self):
        print('Please, enter your information')
        website = input('Website:')
        user = input('User:')
        password = input('Password:')
        user_info = {'Website': website,
                     'User': user,
                     'Password': password}
        self.credentials.append(user_info)
        return self.credentials


list1 = []
register1 = PasswordManager(list1)
print(register1.register_login_info())
