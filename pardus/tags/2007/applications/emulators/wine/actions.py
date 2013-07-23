#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("tools/Makefile.in", "update-desktop-database", "")
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("LDFLAGS", "")
    autotools.autoconf()
    autotools.configure("--with-opengl --with-curses")

def build():
    autotools.make("depend")
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ANNOUNCE", "AUTHORS", "BUGS", "ChangeLog", "DEVELOPERS-HINTS", "README", "documentation/README.*")

    pisitools.remove("/usr/bin/wineshelllink")
    pisitools.removeDir("/usr/share/applications")

    pisitools.doexe("tools/killwineapps/killwineapps", "/usr/bin")
    pisitools.domo("tools/killwineapps/po/tr.po", "tr", "killwineapps.mo")
