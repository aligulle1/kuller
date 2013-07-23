#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"
WorkDir = "unionfs-1.4"

def setup():
    # disable debug and add acl support
    shelltools.echo("fistdev.mk", "UNIONFS_DEBUG_CFLAG=")
    shelltools.echo("fistdev.mk", "EXTRACFLAGS=\"-DUNIONFS_NDEBUG -DUNIONFS_XATTR\"")

    # prefix correction
    pisitools.dosed("Makefile", "PREFIX   = /usr/local", "PREFIX   = %s/usr" % get.installDIR())
    pisitools.dosed("Makefile", "MODPREFIX=", "MODPREFIX= %s" % get.installDIR())
    pisitools.dosed("Makefile", "MANDIR   = \${PREFIX}/man", "MANDIR   = ${PREFIX}/share/man")
    pisitools.dosed("Makefile", "-/sbin/depmod", "#-/sbin/depmod")

    # don't use uname for determine kernel version
    pisitools.dosed("Makefile", "^KVERS=.*", "KVERS=%s" % get.curKERNEL())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosbin("snapmerge")
    pisitools.dodoc("INSTALL", "NEWS", "README", "ChangeLog", "patch-kernel.sh")
