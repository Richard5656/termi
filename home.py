
import subprocess
import os
import sys

print("Log in please!")
# Start reading username.txt and password files.
with open("IGNORE/user/username.data", 'r') as u, open("IGNORE/user/password.data", 'r') as p:
    username = u.read()
    password = p.read()
    l_u = input("Enter your username: ")
    l_p = input("Enter your password: ")
    # If the user typed there username and password and both match up to the txt files allow them to login.
    if username == l_u and password == l_p:
        # say to the user it has sucessfully logged in! Otherwise if the username or password is wrong Say Exiting.
        print("""░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝""")

        print("""
        [1] System info
        [2] Exit safley
        [3] Cmatrix
        [4] Reboot the computer.
        [5] Print a hello world.
        [6] Browser.
        [7] Custom Terminal | TermI Built in terminal
        [8] Firefox | If you don't have firefox installed Don't launch
        [9] Google Chrome | if you don't have Chrome Don't launch
        [10] Clock.
        """)
        type = input(">>>: ")

        if type == '1':
            # Cd into the directory
            os.chdir('IGNORE')
            subprocess.call("python neofetch.py", shell=True)

        if type == '2':
            # cd into the directory
            os.system('exit')
            

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
            os.chdir('IGNORE')
            subprocess.call("python browser.py", shell=True)

        if type == '7':
            os.chdir('IGNORE')
            subprocess.call("python CUSTERM.py", shell=True)

        if type == '8':
            os.system('firefox-bin')
            os.system('firefox')
        
        if type == '9':
            os.system('google-chrome')

        if type == '10':
            os.chdir('IGNORE')
            subprocess.call("python clock.py", shell=True)


       # if get username or password just exit out and print that statement.
    else:
        print("Exiting... you may be typed your username or password wrong.")

