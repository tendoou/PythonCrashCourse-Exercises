from Admin import Admin

admin_privileges = ['can ban user',
                    'can add post',
                    'can delete user']

admin_exercise = Admin('diego', 'beltran', 29, 'culiacan')

# It will execute a second call from the father class,
# i should import modules only with class or functions, without statements.
admin_exercise.privileges.set(admin_privileges)
admin_exercise.privileges.display()
