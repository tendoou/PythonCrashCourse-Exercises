current_users = ['teNDoou', 'areks', 'Kilito', 'AnikA', 'CaTalInA']
new_users = ['Tendoou', 'aReks', 'hagane']

current_users_lower = [x.lower() for x in current_users] #Creamos una copia cambiando todo a minusculas.

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, choose another user name.")
    else:
        print(f"User name available.")
