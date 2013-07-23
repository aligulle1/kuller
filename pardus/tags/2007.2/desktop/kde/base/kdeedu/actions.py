#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "kvoctrain")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # http://bugs.pardus.org.tr/show_bug.cgi?id=5719
    pisitools.remove("/usr/kde/3.5/share/apps/blinken/fonts/steve.ttf")
