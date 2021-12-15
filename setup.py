print("""████████╗███████╗██████╗░███╗░░░███╗██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝""")

register_username = input("Set a username: ")
with open('IGNORE/user/username.data', 'w') as f:
    f.writelines(register_username)
register_password = input("Set a password: ")
with open('IGNORE/user/password.data', 'w') as f:
    f.writelines(register_password)
    print("Username and password has completed sucessfully!")

