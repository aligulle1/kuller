#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", get.LDFLAGS() + "-Wl,-z,now")
    libtools.libtoolize("--copy --force")
    autotools.configure("--enable-music \
                         --enable-dfl-baud=57600 \
                         --enable-resmgr \
                         --sysconfdir=/etc/minicom")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/minicom")
    pisitools.insinto("/etc/minicom", "doc/minirc.dfl")
    pisitools.remove("/usr/bin/xminicom")
    pisitools.remove("/usr/share/man/man1/xminicom.1")
    pisitools.dodoc("doc/minicom.FAQ")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "NEWS")
