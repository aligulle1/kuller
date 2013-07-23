#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mm2.7"

def setup():
    shelltools.cd("src")
    shelltools.chmod("configure")

    autotools.configure()

def build():
    shelltools.cd("src")

    autotools.make()

def install():
    shelltools.cd("src")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "CREDITS", "README")
    
    shelltools.unlink("man/mmencode.1")
    pisitools.doman("man/*", "debian/mimencode.1", "debian/mimeit.1")

