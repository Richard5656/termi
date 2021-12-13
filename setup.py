import time

with open('user/info.data', 'w') as f:
    f.writelines("1")


print("""████████╗███████╗██████╗░███╗░░░███╗██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝""")

register_username = input("Set a username: ")
with open('user/datapass.pass', 'w') as f:
    f.writelines(register_username)

register_password = input("Set a password: ")
with open('user/dataname.pass', 'w') as f:
    f.writelines(register_password)

print("Username and password has been created!")
print("Setup is complete!")
print("Opening home page..")
time.sleep(0.10)
import home.py

