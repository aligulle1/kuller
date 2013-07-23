#! /bin/sh

link=""
icon=""

while [ $# -gt 0 ]
do
  case "$1" in
    --desktop) shift 1 ;;
    --menu)    shift 1 ;;
    --path)    shift 2 ;;
    --link)    link="$2"; shift 2 ;;
    --args)    shift 2 ;;
    --icon)    icon="$2"; shift 2 ;;
    --descr)   shift 2 ;;
    --workdir) shift 2 ;;
  esac
done

if [ -f "$icon" ]
then
    xpmicon="$(echo $link | sed s,/,_,g)"
    iconsdir="$HOME/.local/share/icons"

    mkdir -p "$iconsdir"
    cp "$icon" "$iconsdir/$xpmicon.xpm"
fi

[ -d "$HOME/.local/share/applications/wine" ] || mkdir -p -m 755 $HOME/.local/share/applications/wine

wine-update-menus.py
exit 0
