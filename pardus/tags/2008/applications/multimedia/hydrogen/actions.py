#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.configure("--prefix=/usr \
                         --enable-jack \
                         --enable-alsa \
                         --enable-ladspa \
                         --enable-lrdf-support \
                         --enable-oss-support")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/hydrogen/data/doc/updateManuals.sh")
    pisitools.dosym("/usr/share/hydrogen/data/img/gray/icon.svg", "/usr/share/icons/hicolor/scalable/apps/hydrogen.svg")

    pisitools.doman("data/doc/man/C/hydrogen.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
