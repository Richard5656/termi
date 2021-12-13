import os
import sys

print("Log in please!")
# Start reading username.txt and password files.
with open("user/datapass.pass", 'r') as u, open("user/dataname.pass", 'r') as p:
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
            # Cd into the directory
            sys.path.append('IGNORE')
            import neofetch.py

        if type == '2':
            # cd into the directory
            sys.path.append('IGNORE')
            import CUCP.py

        if type == '3':
            # Ignore the os.system code. What they are supposed to do is add support for diffrent linux distro's.
            # For example if the first one (Emerge) is a invalid command it will move on to the second command and see 
            # Which works for diffrent Linux distros.
            os.system('sudo emerge --ask --autounmask cmatrix')
            os.system('sudo apt-get install cmatrix')
            os.system('sudo pacman -S cmatrix')
            os.system('cmatrix')

        if type == '4':
            # Most likely only works if the user is running home.py as root
            os.system('reboot')
        
        if type == '5':
            print("Hello world!")

        if type == '6':
            # cd into the Ignore directory to import a diffrent .py file
            sys.path.append('IGNORE')
            import browser.py

        

    # if get username or password just exit out and print this statement:
    else:
        print("Exiting... you may be typed your username or password wrong.")

