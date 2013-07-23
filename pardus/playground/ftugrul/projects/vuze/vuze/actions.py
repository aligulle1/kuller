#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    deldirs = ["org/gudy/azureus2/platform/macosx",
               "org/gudy/azureus2/ui/swt/osx",
               "org/gudy/azureus2/ui/swt/test",
               "org/bouncycastle"]
    delfiles = ["/org/gudy/azureus2/ui/swt/win32/Win32UIEnhancer.java",
                "org/gudy/azureus2/ui/console/multiuser/TestUserManager.java"]
    for dirs in deldirs:
        shelltools.unlinkDir("%s/%s" % (get.workDIR(),dirs))
    for files in delfiles:
        shelltools.unlink("%s/%s" % (get.workDIR(),files))

    shelltools.makedirs("%s/build/libs" % get.workDIR())

def build():
    shelltools.export("ANT_OPTS", "-Xmx192m")
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "dist/Azureus2.jar")

    pisitools.dodoc("*.txt")
