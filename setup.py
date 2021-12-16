import time
import subprocess

print("""████████╗███████╗██████╗░███╗░░░███╗██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝""")

print("Have you done the setup already?")
print("""
[1] Continue with the setup.
[2] I have already done the setup.
""")

type = input(">>>: ")

if type == '1':
    register_username = input("Enter a username: ")
    with open('IGNORE/user/username.data', 'w') as f:
        f.writelines(register_username)
        print("username has been created")
    register_password = input("Enter a password: ")
    with open('IGNORE/user/password.data', 'w') as f:
        f.writelines(register_password)
        print("username and password has been created sucessfully")
        subprocess.call("python home.py", shell=True)

if type == '2':
    print("launching home.py...")
    time.sleep(7)
    subprocess.call("python home.py", shell=True)
