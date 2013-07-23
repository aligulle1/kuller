#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure('--with-icondir=/usr/share/pixmaps \
                         --with-ogg=/usr \
                         --with-mp3=/usr \
                         --enable-ogg \
                         --enable-mp3 \
                         --with-distributor="Pardus" \
                         --disable-debug')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/share/doc/warzone2100", get.srcTAG())
