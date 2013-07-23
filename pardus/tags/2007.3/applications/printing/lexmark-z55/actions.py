#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "./"
NoStrip = "/"

src = "lexmarkz55-CUPS-1.0-1.gz.sh"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            if name.endswith(".h") or name.endswith(".ppd"):
                shelltools.chmod(os.path.join(root, name), 0644)
            elif name.endswith(".a") or name.endswith(".la"):
                shelltools.unlink(os.path.join(root, name))
            else:
                shelltools.chmod(os.path.join(root, name), 0755)


def unpackrpm(_f):
    tgz = _f.replace(".rpm", ".tar.gz")

    if os.path.exists(tgz):
        shelltools.unlink(tgz)

    shelltools.system("rpm2targz %s" % _f)
    shelltools.system("tar zxvf %s" % tgz)

def setup():
    shelltools.system("tail -n +143 %s | tar --wildcards -xzf - '*.rpm'" % src)

    for f in shelltools.ls("*.rpm"):
        unpackrpm(f)

    d = "usr/share/cups/model"
    shelltools.makedirs("%s/C" % d)

    for f in shelltools.ls(d):
        if not shelltools.isDirectory("%s/%s" % (d,f)):
            shelltools.move("%s/%s" % (d,f), "%s/C/" % d)

    for f in shelltools.ls("usr/share/cups/model/C/*.ppd.gz"):
        shelltools.system("gunzip -f %s" % f)

    fixperms("usr")

def install():
    pisitools.dodir("/usr")
    for d in shelltools.ls("usr/"):
        shelltools.copytree("usr/%s" % d, "%s/usr/" % get.installDIR())

    for f in ["z55core", "z55printer", "z55printjob"]:
        t = "liblex%s.so.0" % f
        pisitools.dosym("%s.0.0" % t, "/usr/lib/%s" % t)

    pisitools.removeDir("/usr/include")
    pisitools.dodoc("README")

