import requests


class Credentials:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def is_valid(self):
        request = requests.get(f'http://{self.website}')
        if request.status_code == 200:
            return True
        else:
            return False
