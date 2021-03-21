class Credentials:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def is_valid(self):
        return True