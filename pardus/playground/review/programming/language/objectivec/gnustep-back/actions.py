#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("GNUSTEP_MAKEFILES", "/usr/share/GNUstep/Makefiles")
    shelltools.export("GNUSTEP_INSTALLATION_DOMAIN", "SYSTEM")
    autotools.configure("--enable-glx \
                        --enable-server=x11 \
                        --enable-graphics=xlib")

def build():
    autotools.make("messages=yes fonts=no")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ANNOUNCE", "ChangeLog", "COPYING*", "NEWS", "README")
