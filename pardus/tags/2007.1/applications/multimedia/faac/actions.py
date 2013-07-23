#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "faac"

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.7")
    shelltools.export("WANT_AUTOCONF", "2.5")

    shelltools.chmod("bootstrap", 0755)
    shelltools.system("./bootstrap")
    libtools.gnuconfig_update()

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL", "NEWS", "README", "TODO", "docs/libfaac.pdf")

