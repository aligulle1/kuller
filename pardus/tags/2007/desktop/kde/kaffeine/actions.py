#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--without-gstreamer")

def build():
    kde.make()

def install():
    kde.install()

    # kdelibs already have this
    pisitools.remove("/usr/kde/3.5/share/mimelnk/application/x-mplayer2.desktop")

    # This line can be removed when Turksat data is merged
    pisitools.remove("/usr/kde/3.5/share/apps/kaffeine/dvbdata.tar.gz")
