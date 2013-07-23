#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "")
    shelltools.export("LDFLAGS", "")

    autotools.autoconf()
    autotools.aclocal()
    autotools.automake()

    shelltools.export("grub_cv_prog_objcopy_absolute", "yes")

    autotools.configure("--libdir=/lib \
                        --datadir=/usr/lib/grub \
                        --exec-prefix=/ \
                        --disable-auto-linux-mem-opt")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.newdoc("docs/menu.lst", "grub.conf.sample")
