#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 

def setup():
    autotools.configure("--prefix=/usr \
                         --with-x \
                         --with-ssl \
                         --with-slang")

def configure():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/terminfo")
    autotools.rawInstall("DESTDIR=%s \
                        TERMINFO=%s/usr/share/terminfo" % (get.installDIR(), get.installDIR()))
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README*", "TODO", "linux/README")
    pisitools.dohtml("doc/*")
