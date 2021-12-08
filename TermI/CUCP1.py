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

        
            


     
