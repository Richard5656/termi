import os

print("""
[1] Terminal browser.
[2] Python browser.
""")

type = input(">>>: ")

if type == '1':
    # Ignore the os.system code They just add install link commands depending what what distro people use.
    os.system('sudo apt-get install links')
    os.system('sudo pacman -S links')
    os.system('sudo emerge --ask links')
    os.system('links google.com')
 
 if type == '2':
    import brows.py
