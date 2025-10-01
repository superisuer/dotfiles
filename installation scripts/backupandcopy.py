import os
from pathlib import Path

print("BACKUP AND COPY THE NEW DOTFILES")
def restore():
    config_dir = Path.home() / ".config"

    for item in config_dir.iterdir():  # Not gonna lie this was skidded
        if ".bak" in item.name:
            new_name = item.name.replace(".bak", "")
            item.rename(config_dir / new_name)
            print(f"Restored: {item.name} -> {new_name}")

def backup():
    print("Are you sure this will delete some of your configs before restore the backups? (Y/N)")
    print("Backups avaible:")
    os.system("ls $HOME/.config | grep .bak")

    choice = input()
    if choice.upper() == "Y":
        print("Removing...")
        os.system("rm -r $HOME/.config/hypr")
        os.system("rm -r $HOME/.config/fastfetch")
        os.system("rm -r $HOME/.config/waybar")
        os.system("rm -r $HOME/.config/kitty")
        print("REMOVED! Starting to restore")

        restore()
        print("Done!")
    elif choice.upper() == "N":
        print("Okay!\n\n")
        choose()

def install():
    print("Are you sure? (Y/N)")
    choice = input()

    if choice.upper() == "Y":
        print("We will backup the old ones first! this will remove your old backups before you sure? (Y/N)")
        choice2 = input()

        if choice2.upper() == "Y":
            os.system("rm -r $HOME/.config/hypr.bak")
            os.system("rm -r $HOME/.config/kitty.bak")
            os.system("rm -r $HOME/.config/waybar.bak")
            os.system("rm -r $HOME/.config/fastfetch.bak")
            print("Old backups removed, making new ones!")

            os.system("mv -f $HOME/.config/hypr $HOME/.config/hypr.bak")
            os.system("mv -f $HOME/.config/kitty $HOME/.config/kitty.bak")
            os.system("mv -f $HOME/.config/fastfetch $HOME/.config/fastfetch.bak")
            os.system("mv -f $HOME/.config/waybar $HOME/.config/waybar.bak")
            print("New backups Done!")

            os.system("cp -r $HOME/dotfiles/.config/* $HOME/.config/")
            os.system("cp -r $HOME/dotfiles/base_scripts/scripts $HOME/")
            print("Successfuly installed! do you want to reboot now? (Y/N) if you use anything else nothing will happens")
            choice3 = input()
            if choice3.upper() == "Y":
                os.system("reboot")
            
    elif choice.upper("N"):
        print("Okay!\n\n")
        choose()
    else:
        print("Not recognized! asking again...\n\n")
        install()

def choose():
    print("What you want to do? | Abort (X) | Restore backup (R) | Install the dotfiles (I)")
    choice = input()
    if choice.upper() == "X":
        return
    elif choice.upper() == "R":
        backup()
    elif choice.upper() == "I":
        install()
    else:
        print("Not recognized asking again...\n\n")
        choose()

choose() # Needs it to start lol
