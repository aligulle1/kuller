#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"

data = "/usr/share/egoboo"
docs = ["Changelog.txt", "Egoboo %s Manual.pdf" % get.srcVERSION(), "License.pdf", "Readme.txt"]


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for f in ["Changelog.txt", "Readme.txt"]:
        pisitools.dosed(f, "\r")

def install():
    pisitools.dodir(data)
    for d in os.listdir("./"):
        if shelltools.isDirectory(d):
            fixperms(d)
            pisitools.insinto(data, d)

    for f in docs:
        pisitools.dodoc(f, destDir="egoboo")

