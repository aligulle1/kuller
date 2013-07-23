#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    autotools.autoreconf()
    autotools.rawConfigure("--libdir=/lib \
                            --enable-fakeroot=%s \
                            --host=%s \
                            --enable-isadir=/lib/security" % (get.installDIR(),get.HOST()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s LDCONFIG=:" % get.installDIR())

    pisitools.doman("doc/man/*.[0-9]")

    pisitools.removeDir("/usr/share/doc/pam/")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")

    # need this for pam_console
    pisitools.dodir("/var/run/console")
