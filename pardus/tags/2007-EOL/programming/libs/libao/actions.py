#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize()
    autotools.configure("--enable-alsa09 \
                        --disable-alsa09-mmap \
                        --enable-arts \
                        --disable-esd \
                        --enable-nas \
                        --enable-shared \
                        --disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/share/doc")
    pisitools.dodoc("AUTHORS", "CHANGES", "README", "TODO")
    pisitools.dohtml("doc/*.html") 
