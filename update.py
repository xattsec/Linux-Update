import os
import platform

update = input("Would you like to update your machine?:\n")
if update.lower() == "yes":
    x = "debian"
    v = "arch"
    z = "fedora"
    print("Checking distro...")
    if v in platform.platform():
        os.system('sudo pacman -Syu')
        os.system('yay -Syu')
        print("Done updating.")
    elif x in platform.platform():
        os.system('sudo apt update && sudo apt upgrade -y')
        print("Done updating.")
    elif v in platform.platform():
        os.system('sudo dnf update && sudo dnf upgrade -y')
        print("Done updating.")
    else:
        print("Could not find OS in selection.")
else:
    exit()
