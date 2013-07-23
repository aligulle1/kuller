#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "ktorrent-2.1beta1"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # This is in kdelibs already
    pisitools.remove("/usr/kde/3.5/share/mimelnk/application/x-bittorrent.desktop")
