#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "qalculate-kde-%s" % get.srcVERSION()

def setup():
    autotools.autoconf()

    kde.configure()
    pisitools.dosed("configure", "\$CXXFLAGS -fno-exceptions", "$CXXFLAGS")

def build():
    kde.make()

def install():
    kde.install()
