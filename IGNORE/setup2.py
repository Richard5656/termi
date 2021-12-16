print("TermI is a project that is supposed to make the linux terminal more easier to use!")
print("Again feel free to Modify the source code and put some bugs in the issues tab!")

print("""
[1] Continue on with the setup.
""")

type = input(">>>: ")

if type == '1':
    r_u = input("Set a username: ")
    with open('user/username.txt', 'w') as f:
        f.writelines(r_u)

    r_p = input("Set a password: ")
    with open('user/password.txt', 'w') as f:
        f.writelines(r_p)

    print("Username and password has been set now launch the home.py file and your done!")
