#!/bin/bash

REPOSRC="https://github.com/undiabler/arch-i3-wm.git"
LOCALREPO="$HOME/.config/i3"

# We do it this way so that we can abstract if from just git later on
LOCALREPO_VC_DIR=$LOCALREPO/.git


echo "Install i3wm..."
sudo pacman -S --needed --noconfirm i3-gaps i3lock i3blocks git python-jinja python-requests rxvt-unicode scrot compton

echo "Install fonts..."
sudo pacman -S --needed --noconfirm ttf-ubuntu-font-family terminus-font
#yaourt --noconfirm --needed awesome-terminal-fonts-git

echo "Install i3 autoconfig..."
if [ ! -d $LOCALREPO_VC_DIR ]
then
    git clone $REPOSRC $LOCALREPO
else
    cd $LOCALREPO
    git pull $REPOSRC
fi

echo "Done!"