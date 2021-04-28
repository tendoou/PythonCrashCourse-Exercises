import random
import string


class PasswordGenerator:
    def __init__(self):
        self.password = []
        self.password_length = 12
        self.password_characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        for x in range(self.password_length):
            self.password.append(random.choice(self.password_characters))
        new_password = ''.join(self.password)
        return new_password


#password1 = PasswordGenerator()
#print(password1.generate_password())