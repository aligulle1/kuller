#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    #shelltools.export("QTDIR", get.qtDIR())
    shelltools.export("CPPFLAGS", "%s -I/usr/include/libavcodec -I/usr/include/libavformat -I/usr/include/libavdevice -I/usr/include/libavutil -I/usr/include/libpostproc -I/usr/include/libswscale")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=%s" % get.kdeDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())
