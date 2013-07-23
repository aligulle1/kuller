#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def setup():
    shelltools.export("AT_M4DIR", "m4")
    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-fi")

    shelltools.export("COM_netscape", "no")
    shelltools.export("LANG", "C")

    autotools.configure("--sysconfdir=/etc/a2ps \
                         --includedir=/usr/include \
                         --enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install("sysconfdir='%s/etc/a2ps' \
                       includedir='%s/usr/include' \
                       lispdir='%s/usr/share/emacs/site-lisp/%s'" % (get.installDIR(), get.installDIR(), get.installDIR(), get.srcTAG()))

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "ChangeLog", "FAQ", "NEWS", "README*", "THANKS", "TODO")
    pisitools.remove("/usr/lib/liba2ps.a")
