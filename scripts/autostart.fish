#!/usr/bin/env fish

# --- Configuration ---
set WALLPAPER "$HOME/Pictures/Wallpapers/wallpaper_space.png"

# --- Set wallpaper ---
if test -f $WALLPAPER
    /usr/bin/feh --bg-scale $WALLPAPER
else
    echo "Wallpaper not found: $WALLPAPER"
end

# --- Swap Caps Lock and Escape ---
setxkbmap -option caps:swapescape

