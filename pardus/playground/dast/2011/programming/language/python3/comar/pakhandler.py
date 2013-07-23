# -*- coding: utf-8 -*-

import piksemel
import os
import os.path
from subprocess import *

pythonPath="/usr/lib/python3.2"

def byteCompile(filepath):
    doc = piksemel.parse(filepath)
    paths = []
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".py") and not path.startswith("usr/share/doc/"):
            paths.append("/"+path)
    # compile .py files in batches of 200 files to prevent overflow of args buffer
    cmd = ["/usr/bin/python3", "%s/py_compile.py" % pythonPath]
    while len(paths) >= 200:
        call(cmd + paths[0:200])
        del paths[0:200]
    if paths:
        call(cmd + paths)

def removeByteCompiled(filepath):
    doc = piksemel.parse(filepath)
    # collect paths in set and then remove empty ones
    dirs = set()
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".py"):
            d, f = os.path.split(path)
            r, e = os.path.splitext(f)
            dirs.add(d)
            dirs.add("%s/__pycache__" % d)
            try:
                os.unlink("/%sc" % path)
            except OSError:
                pass
            try:
                os.unlink("/%so" % path)
            except OSError:
                pass
            try:
                os.unlink("%s/__pycache__/%s.cpython-32%sc" % (d,r,e))
            except OSError:
                pass
            try:
                os.unlink("%s/__pycache__/%s.cpython-32%so" % (d,r,e))
            except OSError:
                pass
    # remove empy dirs
    dirs = list(dirs)
    dirs.sort(reverse=True)
    for d in dirs:
        if not os.listdir(d):
            os.rmdir(d)

def setupPackage(metapath, filepath):
    byteCompile(filepath)

def postCleanupPackage(metapath, filepath):
    removeByteCompiled(filepath)
