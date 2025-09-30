import os

aur_packages = "ttf-google-sans-code-nf zen-browser-bin"
pacman_packages = "swww kvantum hyprland waybar fastfetch kitty wofi hyprpaper swaync fish pavucontrol ttf-jetbrains-mono ttf-jetbrains-mono-nerd dolphin"

print("WELCOME TO THE PACKAGES INSTALLATION, SELECT A OPTION PLEASE")

def pacman():
    os.system("sudo pacman -S " + pacman_packages + " --needed")
    print("Do you wish to use FISH as your default SHELL? (Y/N)")
    
    choice = input()
    if choice.upper() == "Y":
        os.system("chsh -s /usr/bin/fish")
        print("Done!")
    
def update():
    print("Do you want to syncronize and update your system first? (Y/N)")
    choice2 = input()

    if choice2.upper() == "Y":
        os.system("sudo pacman -Syu")
    elif choice2.upper() == "N":
        print("Okay!")
    else:
        print("Not a valid option try again \n\n\n\n\n\n")
        update()

def aur():
    print("Select the AUR manager | YAY (Y) | Paru (P)")
    choice3 = input()

    if choice3.upper() == "Y":
        os.system("sudo pacman -S yay --needed") # ignore if your distro pacman don't comes with yay
        os.system("yay -S " + aur_packages + " --needed")
    elif choice3.upper() == "P":
        os.system("sudo pacman -S yay --needed") # ignore if your distro pacman don't comes with paru
        os.system("paru -S " + aur_packages + " --needed")

def choose():
    print("Install all (A) | Install Pacman packages (P) | Install AUR packages (U) | Abort (X) | Skip (S)")
    choice = input()

    if choice.upper() == "A" or choice.upper() == "P" or choice.upper() == "U":
        update()
        if choice.upper() == "A":
            pacman()
            aur()
        elif choice.upper() == "P":
            pacman()
        elif choice.upper() == "U":
            aur()
        elif choice.upper() == "S":
           print("Okay")
    elif choice.upper() == "X":
        return
    else:
        print("Invalid option, try again\n\n\n\n\n")
        choose()

choose() # MAIN FUNCTION OF ALL!
print("Step 1 - Installation of packages DONE!")
