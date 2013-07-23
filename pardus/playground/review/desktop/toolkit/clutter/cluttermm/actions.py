#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cluttermm-%s" % get.srcVERSION().split("_")[0]

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --enable-shared \
                         --disable-static")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/share/doc/cluttermm-1.0/*","/usr/share/doc/cluttermm/")
    pisitools.removeDir("/usr/share/doc/cluttermm-1.0/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*", "NEWS")
