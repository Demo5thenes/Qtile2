#!/bin/bash

# You can call this script like this:
# $./brightness.sh up
# $./brightness.sh down

case $1 in
    up)
        brightnessctl -q set 5%+
    ;;
    down)
        brightnessctl -q set 5%-
    ;;
esac