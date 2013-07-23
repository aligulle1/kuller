#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make("prefix=/usr \
                nolirc=1")

def install():
    scons.install("prefix=%s/usr install" % get.installDIR())
    pisitools.dodoc("AUTHORS", "README", "TRANSLATORS")
