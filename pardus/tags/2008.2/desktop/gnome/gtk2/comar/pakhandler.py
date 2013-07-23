#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateIconCache(filepath):
    parse = piksemel.parse(filepath)
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/icons/hicolor"):
            os.system("/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor")

def setupPackage(metapath, filepath):
    updateIconCache(filepath)

def cleanupPackage(metapath, filepath):
    updateIconCache(filepath)
