class User:
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


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=[]):
        self.__privileges = privileges

    def set(self, privileges):
        if privileges:
            self.__privileges = privileges
        else:
            print('ERROR: Cannot set empty privilege list')

    def has_permission(self, privilege_name):
        for privilege in self.__privileges:
            if privilege == privilege_name:
                return True

        return False

    def display(self):
        print(f"\nYour privileges as admin are:")
        if self.__privileges:
            for privilege in self.__privileges:
                print(f"-{privilege}")
        else:
            print("-This user has no privileges.")


admin_privileges = ['can ban user',
                    'can add post',
                    'can delete user']

new_admin = Admin('diego', 'beltran', 29, 'culiacan')

new_admin.privileges.set(admin_privileges)
new_admin.privileges.display()
can_ban_users = new_admin.privileges.has_permission('can reactivate user')

print('Admin can ban users? ' + str(can_ban_users))