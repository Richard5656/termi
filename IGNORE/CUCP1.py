import os

print("username and password seems valid.")
print("Continuing...")
register_username = input("Create a new username: ")
with open('user/username.data', 'w') as f:
    f.writelines(register_username)
register_password = input("Create a new password: ")
with open('user/password.data', 'w') as f:
    f.writelines(register_password)
    print("Username and password has changed!")
    print("Please relaunch the home.py")
