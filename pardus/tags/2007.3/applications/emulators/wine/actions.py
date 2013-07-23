#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("tools/Makefile.in", "update-desktop-database", "")
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("LDFLAGS", "")

    autotools.autoconf()
    autotools.configure("--with-opengl \
                         --with-curses")

def build():
    autotools.make("depend")
    autotools.make()

def install():
    autotools.install()

    pisitools.doexe("tools/killwineapps/killwineapps", "/usr/bin")
    pisitools.domo("tools/killwineapps/po/tr.po", "tr", "killwineapps.mo")

    pisitools.remove("/usr/bin/wineshelllink")
    pisitools.removeDir("/usr/share/applications")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "BUGS", "ChangeLog", "COPYING.LIB", "LICENSE", "README", "documentation/README.*")
