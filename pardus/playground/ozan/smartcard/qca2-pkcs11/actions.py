#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    pisitools.dolib("lib/libqca-pkcs11.so", "%s/crypto" % qt4.plugindir)

    pisitools.dodoc("COPYING", "README")
