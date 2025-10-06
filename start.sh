echo " ______         ,-----.  ,---------.  ________ .-./\`)   .---.       .-''-.     .-'''-.  ";
echo "|    _ \`''.   .'  .-,  '.\\          \\|        |\\ .-.')  | ,_|     .'_ _   \\   / _     \\ ";
echo "| _ | ) _  \\ / ,-.|  \\ _ \\\`--.  ,---'|   .----'/ \`-' \\,-./  )    / ( \` )   ' (\`' )/\`--' ";
echo "|( ''_'  ) |;  \\  '_ /  | :  |   \\   |  _|____  \`-'\`\"\`\\  '_ '\`) . (_ o _)  |(_ o _).    ";
echo "| . (_) \`. ||  _\`,/ \\ _/  |  :_ _:   |_( )_   | .---.  > (_)  ) |  (_,_)___| (_,_). '.  ";
echo "|(_    ._) ': (  '\\_/ \\   ;  (_I_)   (_ o._)__| |   | (  .  .-' '  \\   .---..---.  \\  : ";
echo "|  (_.\\.' /  \\ \`\"/  \\  ) /  (_(=)_)  |(_,_)     |   |  \`-'\`-'|___\\  \`-'    /\\    \`-'  | ";
echo "|       .'    '. \\_/\`\`\".'    (_I_)   |   |      |   |   |        \\\\       /  \\       /  ";
echo "'-----'\`        '-----'      '---'   '---'      '---'   \`--------\` \`'-..-'    \`-...-'   ";
echo "                                                                                        ";

echo "Installing python if necessary"
sudo pacman -S python --needed

echo "Starting packages install the dotfiles NEED to be in your HOME path"
python $HOME/dotfiles/"installation scripts"/packages.py

echo "Starting backup and copy the dotfiles NEED to be in your HOME path"
python $HOME/dotfiles/"installation scripts"/backupandcopy.py
