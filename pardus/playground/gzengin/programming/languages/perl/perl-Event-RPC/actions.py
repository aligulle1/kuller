#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "Event-RPC-%s" % get.srcVERSION()

def build():
    shelltools.system("perl Makefile.PL")
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("Changes", "README")