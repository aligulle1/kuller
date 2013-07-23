#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

WorkDir="FreeRDP-old"

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--with-smartcard \
                         --with-alsa \
                         --with-dfb \
                         --without-pulse \
                         --without-ffmpeg \
                         --without-x \
                         --without-xvideo \
                         --without-xkbfile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
