#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("gtk-update-icon-cache -f /usr/share/icons/hicolor")
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gthumb")

def preRemove():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gthumb")
