import os
import sys

print("Log in please!")
# Start reading username.txt and password files.
with open("user/username.txt", 'r') as u, open("user/password.txt", 'r') as p:
    username = u.read()
    password = p.read()
    l_u = input("Enter your username: ")
    l_p = input("Enter your password: ")
    # If the user typed there username and password and both match up to the txt files allow them to login.
    if username == l_u and password == l_p:
        # say to the user it has sucessfully logged in! Otherwise if the username or password is wrong Say Exiting.
        print("Welcome!")

        print("""
        [1] System info
        [2] Change username and password
        [3] Cmatrix | You need cmatrix installed.
        [4] Reboot the computer.
        [5] Print a hello world.
        [6] Browser.
        """)
        type = input(">>>: ")

        if type == '1':
            sys.path.append('IGNORE')
            import neofetch.py

        if type == '2':
            sys.path.append('IGNORE')
            import CUCP.py

        if type == '3':
            os.system('cmatrix')

        if type == '4':
            os.system('reboot')
        
        if type == '5':
            print("Hello world!")

        if type == '6':
            sys.path.append('IGNORE')
            import browser.py

        


    else:
        print("Exiting... you may be typed your username or password wrong.")

