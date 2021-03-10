class Users:
    def __init__(self, first_name, last_name, age, country):
        self.name = first_name.title()
        self.last = last_name.title()
        self.age = age
        self.country = country.title()
        self.login_attempts = 0
    def describe_user(self):
        print(f"first name: {self.name}"
              f"\nlast name: {self.last}"
              f"\nage: {self.age}"
              f"\ncountry: {self.country}.")

    def greet_user(self):
        print(f"Hello {self.name}!, you're soo coor.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


first_user = Users('diego', 'beltran', '29', 'méxico')

first_user.describe_user()
first_user.greet_user()

first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.reset_login_attempts()
print(first_user.login_attempts)
