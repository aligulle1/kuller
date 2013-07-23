#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateData(filepath):
    parse = piksemel.parse(filepath)

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/lib/gdk-pixbuf-2.0/2.10.0/loaders"):
            os.system("/usr/bin/gdk-pixbuf-query-loaders > /usr/lib/gdk-pixbuf-2.0/2.10.0/loaders.cache")
            return
        elif path.startswith("usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders"):
            os.system("/usr/bin/gdk-pixbuf-query-loaders-32bit > /usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders.cache")
            return

def setupPackage(metapath, filepath):
    updateData(filepath)

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
