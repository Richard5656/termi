print("Welcome! Are you sure you want to change your username and password? This can not be undone.")

print("""
[1] No Take me back.
[2] Yes Continue.
""")

type = input(">>>: ")

if type == '1':
    import home.py

if type == '2':
    import CUCP1.py
