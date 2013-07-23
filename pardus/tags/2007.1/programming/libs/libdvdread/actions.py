#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools

def setup():
    libtools.gnuconfig_update()
    autotools.autoreconf()
    autotools.configure("--with-libdvdcss=/usr \
                         --disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dobin("src/.libs/*")
    pisitools.domove("/usr/bin/ifo_dump", "/usr/bin", "ifo_dump_dvdread")
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README", "TODO")
