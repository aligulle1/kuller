#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("./m64p_build.sh PREFIX=/usr")

def install():
    shelltools.system("./m64p_install.sh PREFIX=/usr MANDIR=/usr/share/man/man6 DESTDIR=%s" % get.installDIR())
