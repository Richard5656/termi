

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
            import neofetch.py

        if type == '2':
            import CUCP.py
            






    else:
        print("Exiting... you may be typed your username or password wrong.")

