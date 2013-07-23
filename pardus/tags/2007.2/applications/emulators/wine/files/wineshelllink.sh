#! /bin/sh

[ -d "$HOME/.local/share/applications/wine" ] || mkdir -p -m 755 $HOME/.local/share/applications/wine
wine-update-menus.py
exit 0

