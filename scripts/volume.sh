#!/bin/bash

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down

case $1 in
    up)
        pactl set-sink-volume alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.stereo-fallback +5%
    ;;
    down)
        pactl set-sink-volume alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.stereo-fallback -5%
    ;;
    mute)
        pactl set-sink-mute alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.stereo-fallback toggle
    ;;
    
esac