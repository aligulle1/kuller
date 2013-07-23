#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="pptp-1.7.0"

def build():
    autotools.make("DESTDIR=%s" % get.installDIR())

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "DEVELOPERS", "INSTALL",
        "NEWS", "README", "TODO", "USING")

