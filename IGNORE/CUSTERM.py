print("TermI Bulit in terminal 1.2")
print("Type help in the command line to give you a list of commands")
print("To go back. Type back")
import subprocess
import os
import time


while True:
    type = input(">>>: ")
    
    if type == 'help':
        print("Here's a list of commands that you can use! help, reboot, cmatrix, print hello world, go back")
    
    # Ignore the os.system code. They add installing commands for cmatrix
    if type == 'cmatrix':
        print("Installing cmatrix...")
        os.system('sudo pacman -S cmatrix')
        os.system('sudo apt-get install cmatrix')
        os.system('sudo emerge --ask cmatrix')
        os.system('cmatrix')

    if type == 'reboot':
        print("If it fails try running as home.py as root")
        os.system('reboot')

    if type == 'print hello world':
        print("Hello World!")

    if type == 'back':
        os.chdir('../')
        subprocess.call("python home.py", shell=True)

    if type == 'exit':
        os.system('exit')
        os.system('cmatrix')


