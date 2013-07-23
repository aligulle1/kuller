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

WorkDir = "boson-all-%s" % get.srcVERSION()

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system('cmake \
                       -DCMAKE_BUILD_TYPE=None \
                       -DCMAKE_INSTALL_PREFIX=/usr \
                       -DKDEDIR=%s \
                       ..' % get.kdeDIR())

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    pisitools.dodoc("code/AUTHORS", "code/ChangeLog", "code/README*")

    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

