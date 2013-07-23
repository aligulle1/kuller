#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Setup precompiled ghc to bootstrap native ghc
    shelltools.cd("bootstrap")
    autotools.rawConfigure("--prefix=%s/precompiled" % get.workDIR())
    autotools.rawInstall()
    shelltools.cd("..")

    autotools.configure("--with-ghc=%s/precompiled/bin/ghc" % get.workDIR())

    # Enable non-executable stack
    shelltools.echo("driver/ghc/Makefile","GHC_CFLAGS = %s -Wa,--noexecstack"  % get.CFLAGS())
    shelltools.echo("mk/build.mk","SRC_CC_OPTS+=%s -Wa,--noexecstack" % get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%(DESTDIR)s/usr" % {'DESTDIR':get.installDIR()})

    pisitools.dodoc("README","ANNOUNCE","LICENSE","VERSION")
