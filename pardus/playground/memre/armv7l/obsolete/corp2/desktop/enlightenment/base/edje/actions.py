#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-gnu-ld")

    # lua is broken
    #import os
    #makefiles = os.popen("find . -name Makefile").read().split()
    #for file in makefiles:
    #    pisitools.dosed(file, r"\-(L|I)(/usr)(\S*)", "-\\1%(SysRoot)\\2\\3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
