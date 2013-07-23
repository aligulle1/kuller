#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir="digikam-0.9.0-rc2"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # kdelibs already has this
    pisitools.remove("/usr/kde/3.5/share/mimelnk/image/x-raw.desktop")
