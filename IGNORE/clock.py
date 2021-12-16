
import os
import subprocess
import time            # Print the time.
print("The time is " + time.strftime("%m/%d/%y"))

print("""
[1] Go back.
[2] Exit.
""")
print("Would you like to go back?")

type = input(">>>:")

if type == '1':
    os.system('cd ../')
    subprocess.call("python home.py", shell=True)

if type == '2':
    os.system('exit')

