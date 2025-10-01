# huker DOTFILES
![photo of the rice](https://raw.githubusercontent.com/RIOTLaF/dotfiles/refs/heads/main/Images/screenshot.webp)

**NOTE:** NEVER run ./start.sh as super user, it will use sudo when needed and ask for your user password

# Dotfiles Quick install
<img width="190px" src="https://archlinux.org/static/logos/archlinux-logo-white-90dpi.png" alt="Arch Linux" />

## Required packages:
### AUR:
```
ttf-google-sans-code-nf
zen-browser-bin
```

### PACMAN:
```
hyprland
waybar
fastfetch
kitty
wofi
hyprpaper
swaync
fish
pavucontrol
ttf-jetbrains-mono
ttf-jetbrains-mono-nerd
dolphin
python # optional for installation scripts
```

# BINDS

- SUPER + W : BROWSER (Zen browser)
- SUPER + Q : CLOSE ACTIVE
- SUPER + E : FILE MANAGER (Dolphin)
- SUPER + D : MENU
- SUPER + A : TOGGLE SPLIT
- SUPER + V : TOGGLE FLOATING
- SUPER + M : EXIT

# QUICK INSTALL

```
cd $HOME
git clone https://github.com/RIOTLaF/dotfiles.git
cd ~/dotfiles
chmod +x ./start.sh
./start.sh
```
