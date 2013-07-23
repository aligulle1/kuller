#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

WorkDir="FreeRDP-FreeRDP-8e62721"

def setup():
    cmaketools.configure("-DWITH_PULSEAUDIO=ON")

    """
    cmaketools.configure("-DWITH_ALSA=ON \
                          -DWITH_PULSEAUDIO=ON \
                          -DWITH_CUPS=ON \
                          -DWITH_DIRECTFB=ON \
                          -DWITH_X11=ON \
                          -DWITH_FFMPEG=ON \
                          -DWITH_XKBFILE=ON")
    """


def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
