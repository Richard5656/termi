import os

print("""
[1] Terminal browser. | You need links installed for this to work.
[2] Python browser. | Coming soon
""")

type = input(">>>: ")

if type == '1':
    # Ignore the os.system code They just add install link commands depending what what distro people use.
    os.system('sudo apt-get install links')
    os.system('sudo pacman -S links')
    os.system('sudo emerge --ask links')
    os.system('links google.com')
 
