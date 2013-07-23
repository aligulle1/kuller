#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-cpu-specific-optimizations=no \
                         --enable-separate-debug-info=no \
                         --without-java")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosed("%s/usr/lib/%s/site-packages/cspace.pth" % (get.installDIR(), get.curPYTHON()), get.installDIR())

    pisitools.dosed("%s/etc/crystalspace-1.4/vfs.cfg" % get.installDIR(), get.installDIR())

    pisitools.rename("/usr/share/doc/crystalspace-1.4", get.srcTAG())
