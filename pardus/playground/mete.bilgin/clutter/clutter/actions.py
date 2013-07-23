#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    # autotools.configure("--enable-introspection")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-introspection \
                        --with-json=system \
                        --enable-shared ")

def build():
    shelltools.export("HOME", "%s" % get.workDIR())
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "TODO", "README*", "NEWS")

