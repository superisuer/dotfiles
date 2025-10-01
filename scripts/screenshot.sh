#!/bin/bash

DIR="$HOME/Pictures"
mkdir -p "$DIR"

FILE="$DIR/$(date +%F_%H-%M-%S).png"
GEOM=$(slurp)
[ -z "$GEOM" ] && exit

grim -g "$GEOM" "$FILE" && wl-copy < "$FILE" && notify-send "Screenshot saved" "$FILE"
