import os

print("Are you sure you want to change your username and password changes cannot be undone....")
print("""
[1] Yes Continue.
[2] No Exit please.
""")

# Give user abilty to select.
select = input(">>>: ")

if select == '1':
    print("We need to verify its you first.")
    with open("IGNORE/user/username.data", 'r') as u, open("IGNORE/user/password.data", 'r') as p:
        username = u.read()
        password = p.read()
        l_u = input("Enter your current username: ")
        l_p = input("Enter your current password: ")
        if username == l_u and password == l_p:
                import CUCP1.py
        else:
            print("Exiting.... Username or password may be incorrect")                               
