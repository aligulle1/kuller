#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="util-linux-ng-%s" % get.srcVERSION().replace("_","-")

def setup():
    shelltools.export("SUID_CFLAGS", "-fpie")
    shelltools.export("SUID_LDFLAGS", "-pie")

    autotools.configure('--prefix=/ \
                         --enable-nls \
                         --enable-agetty \
                         --enable-cramfs \
                         --enable-partx \
                         --enable-raw \
                         --enable-rdev \
                         --enable-rename \
                         --enable-write \
                         --with-fsprobe=blkid \
                         --with-audit \
                         --disable-init \
                         --disable-kill \
                         --disable-last \
                         --disable-mesg \
                         --disable-reset \
                         --disable-login-utils \
                         --disable-wall \
                         --disable-static')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("HISTORY", "MAINTAINER", "README", "VERSION", "example.files/*")
