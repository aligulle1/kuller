#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS","%s  -fno-rtti -fno-exceptions" % get.CXXFLAGS())

    autotools.configure("--enable-multibyte")

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr")

    autotools.rawInstall("bindir=%(DESTDIR)s/usr/bin \
                          mandir=%(DESTDIR)s/usr/share/man \
                          prefix=%(DESTDIR)s/usr \
                          sysconfdir=%(DESTDIR)s/etc \
                          datadir=%(DESTDIR)s/usr/share \
                          infodir=%(DESTDIR)s/usr/share/info" % {'DESTDIR' : get.installDIR()})

    pisitools.removeDir("/usr/share/doc/groff")
    pisitools.dodoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
