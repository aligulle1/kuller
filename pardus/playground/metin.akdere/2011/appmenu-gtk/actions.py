#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "%s -Wno-error" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -Wno-error" % get.CXXFLAGS())
    autotools.configure("--prefix=/%s \
                         --with-gtk2" % get.defaultprefixDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/etc/X11/Xsession.d/80appmenu" % get.installDIR(), 0755)
    shelltools.unlink("%s/usr/lib/*/*/*/*.a" % get.installDIR())
