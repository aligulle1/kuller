#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "device-mapper.%s" % get.srcVERSION()

def setup():
    autotools.configure("--sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.install('DESTDIR=%(D)s \
                       libdir=%(D)s/lib \
                       includedir=%(D)s/usr/include' % {"D": get.installDIR()})

    pisitools.dolib_a("lib/ioctl/libdevmapper.a")
    libtools.gen_usr_ldscript("libdevmapper.so")

    pisitools.dodoc("COPYING*", "INSTALL", "INTRO", "README", "VERSION", "WHATS_NEW")

