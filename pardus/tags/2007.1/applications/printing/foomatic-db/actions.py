#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from os.path import join

WorkDir = "foomatic-db-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"
foo2zjs = "foo2zjs.files"

def loadFile(_file):
    try:
        f = file(_file)
        d = [a.strip() for a in f]
        f.close()
        return d
    except:
        return None

def setup():
    autotools.configure()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for root, dirs, files in os.walk("%s/usr/share/foomatic/db" % get.installDIR()):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

    # to avoid conflicts with foo2zjs package
    conflicts = loadFile(foo2zjs)
    for l in conflicts:
        c = "%s/%s" % (get.installDIR(), l)
        if os.path.exists(c):
            shelltools.unlink(c)

