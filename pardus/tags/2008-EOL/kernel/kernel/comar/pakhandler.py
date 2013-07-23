# -*- coding: utf-8 -*-

import piksemel
import subprocess

def domodules(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("lib/modules/"):
            kernelVersion = path.split("/")[2]
            subprocess.call(["/sbin/depmod", "-a", "%s" % kernelVersion])
            return

def setupPackage(metapath, filepath):
    domodules(filepath)

def cleanupPackage(metapath, filepath):
    domodules(filepath)
