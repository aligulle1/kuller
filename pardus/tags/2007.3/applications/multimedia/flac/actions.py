#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile.in", "^@FLaC__HAS_XMMS_TRUE")

    autotools.configure("--with-pic \
                         --disable-static \
                         --enable-ogg \
                         --enable-sse")

    # the man page requires docbook2man
    pisitools.dosed("Makefile", "include man", "include")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
