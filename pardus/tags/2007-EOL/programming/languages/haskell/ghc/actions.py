#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-ghc=/usr/bin/ghc")

    # Enable non-executable stack
    shelltools.echo("driver/ghc/Makefile","GHC_CFLAGS = %s -Wa,--noexecstack"  % get.CFLAGS())
    shelltools.echo("mk/build.mk","SRC_CC_OPTS+=%s -Wa,--noexecstack" % get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())

    # Remove references to install directory
    pisitools.dosed("%s/usr/bin/*" % get.installDIR(), get.installDIR(), "")
    pisitools.dosed("%s/usr/lib/ghc-%s/package.conf" % (get.installDIR(),get.srcVERSION()), get.installDIR(), "")

    pisitools.dodoc("README","ANNOUNCE","LICENSE","VERSION")
