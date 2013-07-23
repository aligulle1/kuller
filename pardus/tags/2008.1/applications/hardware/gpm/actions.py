#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "gpm-1.20.3pre4"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--libdir=/usr/lib \
                         --sysconfdir=/etc/gpm")

def build():
    autotools.make("CC=%s AR=%s RANLIB=%s" % (get.CC(), get.AR(), get.RANLIB()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove static link
    pisitools.remove("/usr/lib/libgpm.a")

    pisitools.insinto("/etc/gpm", "conf/gpm-*.conf")

    pisitools.dodoc("BUGS", "Changes", "README", "TODO", "doc/Announce", "doc/FAQ", "doc/README*")
