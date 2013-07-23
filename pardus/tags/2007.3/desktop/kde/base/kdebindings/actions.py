#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE","dcoppython python")
    kde.configure()

def build():
    kde.make("-j1")

def install():
    kde.install()

    perlmodules.fixLocalPod()
