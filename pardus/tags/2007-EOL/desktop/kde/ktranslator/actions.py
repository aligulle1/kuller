#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.removeDir("%s/share/applnk" % get.kdeDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*", "TODO", "COPYING")
