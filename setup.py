

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
            print("Username and password has been set now launch the home.py file and your done!")

