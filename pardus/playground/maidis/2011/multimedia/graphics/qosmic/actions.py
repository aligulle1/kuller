#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("qosmic.pro", "PREFIX = /usr", "PREFIX = %s/usr" % get.installDIR())
    pisitools.dosed("qosmic.pro", "DESTDIR = .", "DESTDIR = ")

    shelltools.system("qmake")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("changes.txt", "COPYING", "README*")
