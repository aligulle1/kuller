#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

def install():
    shelltools.copytree("etc/", "%s/etc" % get.installDIR())
    shelltools.copytree("usr/", "%s/usr" % get.installDIR())
    shelltools.copytree("lib/", "%s/lib" % get.installDIR())
