#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.touch("man/*.1")
    shelltools.chmod("config/*", 0775)

    autotools.configure("--enable-nls")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # use the manpage from man-pages
    pisitools.remove("/usr/share/man/man1/diff.1")

    pisitools.dodoc("ChangeLog", "NEWS", "README")

