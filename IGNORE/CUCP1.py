print("username and password seems vaild")
r_u = input("Set a new username: ")
with open("user/username.txt", 'w') as f:
    f.writelines(r_u)
r_p = input("Set a new password: ")
with open("user/password.txt", 'w') as f:
    f.writelines(r_p)
