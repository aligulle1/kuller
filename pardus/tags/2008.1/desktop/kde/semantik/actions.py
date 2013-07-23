#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("HOME", "%s" % get.workDIR())
    shelltools.system("./waf configure --prefix=/usr/")

def build():
    shelltools.system("./waf")

def install():
    shelltools.system("DESTDIR=%s ./waf install" % get.installDIR())

    pisitools.dodoc("README", "LICENSE.QPL")
