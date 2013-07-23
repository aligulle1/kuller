#!/bin/sh
#
# InnoTek VirtualBox
#
# Copyright (C) 2006 InnoTek Systemberatung GmbH
#
# This file is part of VirtualBox Open Source Edition (OSE), as
# available from http://www.virtualbox.org. This file is free software;
# you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation,
# in version 2 as it comes in the "COPYING" file of the VirtualBox OSE
# distribution. VirtualBox OSE is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY of any kind.
#
# If you received this file as part of a commercial VirtualBox
# distribution, then only the terms of your commercial VirtualBox
# license agreement apply instead of the previous paragraph.

# Load the vboxdrv module
/usr/share/VirtualBox/vbox-python.py

if [ $? = 0 ]; then
    echo "vboxdrv kernel module successfully loaded."
else
    echo "You are not authorized to load vboxdrv module."
    exit 0
fi

CONFIG="/etc/vbox/vbox.cfg"
if [ "$VBOX_USER_HOME" = "" ]; then
    if [ ! -d "$HOME/.VirtualBox" ]; then
        mkdir -p "$HOME/.VirtualBox"
    fi
    LOG="$HOME/.VirtualBox/VBoxSVC.log"
else
    if [ ! -d "$VBOX_USER_HOME" ]; then
        mkdir -p "$VBOX_USER_HOME"
    fi
    LOG="$VBOX_USER_HOME/VBoxSVC.log"
fi


if [ ! -r "$CONFIG" ]; then
    echo "Could not find VirtualBox installation. Please reinstall."
    exit 1
fi

if [ "$1" = "shutdown" ]; then
    SHUTDOWN="true"
elif [ ! -w /dev/vboxdrv ]; then
        echo '/dev/vboxdrv not writable for some reason'
    exit 1
fi

. "$CONFIG_DIR/$CONFIG"

export LD_LIBRARY_PATH="$INSTALL_DIR"

SERVER_PID=`ps -U \`whoami\` | grep VBoxSVC | awk '{ print $1 }'`
if [ "$SHUTDOWN" = "" ] && [ "$SERVER_PID" = "" ]; then
    rm -rf /tmp/.vbox-`whoami`-ipc > /dev/null 2>&1
    [ -f "$LOG.1" ] && mv "$LOG.1" "$LOG.2"
    [ -f "$LOG.0" ] && mv "$LOG.0" "$LOG.1"
    [ -f "$LOG" ] && mv "$LOG" "$LOG.0"
    "$INSTALL_DIR/VBoxSVC" --daemonize > "$LOG" 2>&1
fi

if [ "$SHUTDOWN" = "true" ]; then
    if [ "$SERVER_PID" != "" ]; then
        kill -TERM $SERVER_PID
        sleep 2
    fi
    exit 0
fi

APP=`which $0`
APP=${APP##/*/}
case "$APP" in
  VirtualBox)
    exec "$INSTALL_DIR/VirtualBox" "$@"
  ;;
  VBoxManage)
    exec "$INSTALL_DIR/VBoxManage" "$@"
  ;;
  VBoxSDL)
    exec "$INSTALL_DIR/VBoxSDL" "$@"
  ;;
  VBoxTunctl)
    exec "$INSTALL_DIR/VBoxTunctl" "$@"
  ;;
  vditool)
    exec "$INSTALL_DIR/vditool" "$@"
  ;;
  *)
    echo "Unknown application - $APP"
  ;;
esac
