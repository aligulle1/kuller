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

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-debug \
                         --enable-opengl")

def build():
    shelltools.system("jam")

def install():
    shelltools.system("DESTDIR=\"%s\" jam install" % get.installDIR())

    # We will use a modified desktop file, for now
    pisitools.remove("/usr/share/applications/supertux.desktop")

    pisitools.removeDir("/usr/share/doc/supertux-%s" % get.srcVERSION())
    pisitools.dodoc("WHATSNEW.txt", "README")
