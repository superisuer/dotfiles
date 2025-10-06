  GNU nano 8.6                                                        ./test.sh                                                                     
if [ -f "$HOME/.config/hypr/deleteme" ]; then
    echo "The file exists, its first time!"
    swww-daemon & disown # if not is already running
    swww img $HOME/.config/hypr/wallpaper.jpeg
    rm $HOME/.config/hypr/deleteme # delete the file to prevent this from running again
else
    echo "the file does not exist, all right here"
fi