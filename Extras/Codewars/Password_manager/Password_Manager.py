import json
from credentials import Credentials


# che
class PasswordManager:
    def __init__(self):
        filename = 'password_manager.json'
        try:
            with open(filename) as f:
                entries = json.load(f)
                self.credentials = []
                for entry in entries:
                    self.credentials.append(Credentials(**entry))

        except FileNotFoundError:
            self.credentials = []

    def register_login_info(self, website, username, password):
        credentials = Credentials(website, username, password)
        self.credentials.append(credentials)
        self.create_file()
        return credentials

    def consult_login_info(self, consult):
        for credential in self.credentials:
            if credential.website == consult.lower():
                return credential

    def delete_login_info(self):
        delete = input('Type the website to delete:')
        response = input(f'Are you sure you want to delete the {delete} register? (y/n):')
        if response == 'y':
            for credential in self.credentials:
                print(credential)
                print(type(credential))
                if credential.website == delete.lower():
                    self.credentials.remove(credential)
                    print(f'The entry has been deleted.')
                    self.create_file()
                    return True
        return False

    def create_file(self):
        filename = 'password_manager.json'
        with open(filename, 'w') as f:
            array = [cred.__dict__ for cred in self.credentials]
            json.dump(array, f)
            print('Your login info has been saved successfully.')
            return True
        return False


