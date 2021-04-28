import json
from PasswordGenerator import PasswordGenerator
from credentials import Credentials
import os


# che
class PasswordManager:
    def __init__(self):
        filename = f'{os.path.dirname(os.path.realpath(__file__))}\password_manager.json'
        try:
            with open(filename) as f:
                print(' ??')
                entries = json.load(f)
                self.credentials = []
                for entry in entries:
                    self.credentials.append(Credentials(**entry))

        except FileNotFoundError:
            self.credentials = []

    def register_login_info(self, website, username, password):
        credentials = Credentials(website, username, password)
        """If the user doesn't enter a password the function generates a safe one"""
        if credentials.password == '':
            new_password = PasswordGenerator()
            credentials.password = new_password.generate_password()
        self.credentials.append(credentials)
        self.create_file()
        return credentials

    def consult_login_info(self, consult_website):
        for credential in self.credentials:
            if credential.website == consult_website.lower():
                return credential
        return False

    def delete_login_info(self, delete_website):
        for credential in self.credentials:
            if credential.website == delete_website.lower():
                self.credentials.remove(credential)
                self.create_file()
                return True
        return False

    def create_file(self):
        filename = f'{os.path.dirname(os.path.realpath(__file__))}\password_manager.json'
        with open(filename, 'w') as f:
            array = [cred.__dict__ for cred in self.credentials]
            json.dump(array, f)

            return True



