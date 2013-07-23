#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="q4wine-%s" % get.srcVERSION().replace("_0", "-r")

def setup():
    cmaketools.configure("-DWITH_ICOUTILS=ON -DWITH_WINETRIKS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "copying", "LICENSE", "README")
