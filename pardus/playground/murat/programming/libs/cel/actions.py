#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-optimize-mode-debug-info=no \
                         --enable-separate-debug-info=no \
                         --with-cs-prefix=/usr \
                         --with-python=yes")

def build():
    shelltools.system("jam -qa")

def install():
    shelltools.system("jam -sDESTDIR=%s install" % get.installDIR())

    pisitools.rename("/usr/share/doc/cel-1.4", get.srcTAG())
