#!/usr/bin/python

import piksemel
import os

def updateMimeTypes(filepath):
        parse = piksemel.parse(filepath)
        for icon in parse.tags("File"):
            path = icon.getTagData("Path")
            if path.startswith("usr/share/mime"):
                os.system("/usr/bin/update-mime-database /usr/share/mime")

def setupPackage(metapath, filepath):
    updateMimeTypes(filepath)

def cleanupPackage(metapath, filepath):
    updateMimeTypes(filepath)
