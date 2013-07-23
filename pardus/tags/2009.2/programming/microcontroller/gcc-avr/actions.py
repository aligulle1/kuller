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

def fix_env():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")
    # Bash doesnt activate this path immediately after avr-binutils install
    shelltools.export("PATH", "%s:/opt/avr/bin" % get.ENV("PATH"))

def setup():
    fix_env()

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
    fix_env()
    shelltools.cd("%s/build-avr/" % get.workDIR())
    autotools.make()

def install():
    fix_env()
    shelltools.cd("%s/build-avr/" % get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/opt/avr/man/man7/*")
    pisitools.remove("/opt/avr/info/*")
    pisitools.remove("/opt/avr/lib/libiberty.a")
