#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

def setup():
    shelltools.export("DO_NOT_COMPILE","kandy korn networkstatus")

    autotools.make("-f admin/Makefile.common")
    kde.configure("--with-sasl")

def build():
    kde.make()

def install():
    kde.install()

    # Don't autostart korganizer
    pisitools.remove("%s/share/autostart/korgac.desktop" % get.kdeDIR())
