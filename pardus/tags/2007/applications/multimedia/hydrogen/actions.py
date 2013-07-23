#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("PORTAUDIOPATH", "/usr/lib")
    autotools.configure("--prefix=/usr \
                         --enable-jack \
                         --enable-portaudio \
                         --enable-alsa \
                         --enable-ladspa \
                         --enable-lrdf-support \
                         --enable-oss-support")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
    pisitools.remove("/usr/share/hydrogen/data/doc/updateManuals.sh")
    pisitools.dosym("/usr/share/hydrogen/data/img/gray/icon.svg", "/usr/share/icons/hicolor/scalable/apps/hydrogen.svg")
    pisitools.doman("data/doc/man/C/hydrogen.1")
