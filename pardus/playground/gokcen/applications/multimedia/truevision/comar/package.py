#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system

def postInstall():
    open("/etc/gnome-vfs-mime-magic", "a").write("\n0\tstring\t\tTRUEVISION SCENE\t\t\tapplication/x-truevision")
    system("update-mime-database /usr/share/mime")
