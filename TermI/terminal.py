import os
def setup():
    print("Welcome to TermI! Please continue on with the setup")
    print("Select an option: ")

    print("""
    [1] Continue on with the setup.
    """)

    type = input(">>>: ")

    if type == '1':
            # Make username and password text files to later store them for the home.py For use to login.
            login_username = input("Set a username: ")
            with open('user/username.txt', 'w') as f:
                # put in the username.txt file exactly what the user has typed in the input tag.
                f.writelines(login_username)
            login_password = input("Set a password: ")
            with open('user/password.txt', 'w') as f:
                # Put in the password.txt file exactly what the user has typed in the input tag.
                f.writelines(login_password)
            home()

def neofetch():
    import sys
    import os

    if sys.platform.startswith('freebsd'):
        print("""███████╗██████╗░███████╗███████╗██████╗░░██████╗██████╗░
    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗ OS: FreeBSD
    █████╗░░██████╔╝█████╗░░█████╗░░██████╦╝╚█████╗░██║░░██║ kernel: 13.0
    ██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║ 
    ██║░░░░░██║░░██║███████╗███████╗██████╦╝██████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═════╝░╚═════╝░""")

    if sys.platform.startswith('linux'):
        print("""██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
    ██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝ OS: Linux
    ██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░ kernel: 5.16.6
    ██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░
    ███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗
    ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝""")

    if sys.platform.startswith('win32'):
        print("""░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
    ░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
    ░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░ OS: Windows
    ░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗ 
    ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░""")


    print("Would you like to go back? Type yes to go back or type no to exit")

    type = input(">>>: ")

    if type == 'yes':
        home()

    if type == 'no':
        os.system('exit')




def home():
    os.system("clear")
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
            """)
            type = input(">>>: ")

            if type == '1':
                neofetch()

            if type == '2':
                CUCP()
        else:
            print("Exiting... you may be typed your username or password wrong.")
      
def CUCP():
    print("Welcome! Are you sure you want to change your username and password? This can not be undone.")

    print("""
    [1] No Take me back.
    [2] Yes Continue.
    """)

    type = input(">>>: ")

    if type == '1':
        home()

    if type == '2':
        CUCP1()



def CUCP():
    print("We need to you to login first so we can verify that its you!")
    with open("user/username.txt", 'r') as u, open("user/password.txt", 'r') as p:
        username = u.read()
        password = p.read()
        l_u = input("Please enter your current username: ")
        l_p = input("Please enter your current password: ")
        if username == l_u and password == l_p:
            print("Sucess!")
        else:
            print("Exiting username or password might have been incorrect.")

        if username == l_u and password == l_p:
            makenew_username = input("Set a new username: ")
            # ReWrite the username.txt file according to what the user typed in the input tag.
            with open('user/username.txt', 'w') as f:
                f.writelines(makenew_username)
            makenew_password = input("Set a password: ")
            with open('user/password.txt', 'w') as f:
                f.writelines(makenew_password)

            print("Username and password has changed sucessfully!")
            home()








first_time_check = input("Is this your first time? (y/n)")

if first_time_check == "y":
    setup()
elif first_time_check == "n":
    home()
else:
    print("Invalid")
