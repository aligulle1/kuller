#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gcc-%s" % get.srcVERSION()
NoStrip = "/"

def unset():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")

def setup():
    unset()

    shelltools.makedirs("%s/build-avr" % get.workDIR())
    shelltools.cd("%s/build-avr/" % get.workDIR())

    shelltools.system('%s/%s/configure \
                       --prefix=/opt/avr \
                       --target=avr \
                       --enable-languages="c,c++" \
                       --disable-nls \
                       --disable-libssp \
                       --with-dwarf2' % (get.workDIR(), WorkDir))

def build():
    unset()
    shelltools.cd("%s/build-avr/" % get.workDIR())
    autotools.make()

def install():
    shelltools.cd("%s/build-avr/" % get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/opt/avr/info/dir")
