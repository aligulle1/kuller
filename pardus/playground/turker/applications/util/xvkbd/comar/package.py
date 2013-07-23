#!/usr/bin/python
# -*- coding: utf-8 -*-

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    xsetup = open("/usr/kde/3.5/share/config/kdm/Xsetup", "rb").readlines()
    xsetup.append("xvkbd -geometry -300-100&\n")
    open("/usr/kde/3.5/share/config/kdm/Xsetup", "wb").writelines(xsetup)

def preRemove():
    xsetup = open("/usr/kde/3.5/share/config/kdm/Xsetup", "rb").readlines()
    xsetup.remove("xvkbd -geometry -300-100&\n")
    open("/usr/kde/3.5/share/config/kdm/Xsetup", "wb").writelines(xsetup)


