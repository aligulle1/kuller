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

WorkDir = "hplip-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("hpssd.py", "/usr/bin/env python", "/usr/bin/python")
    autotools.configure("--disable-network-build \
                         --disable-cups-install \
                         --disable-gui-build \
                         --enable-foomatic-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          hpppddir=/usr/share/cups/model/hplip \
                          ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    pisitools.dosym("../libsane-hpaio.la", "/usr/lib/sane/libsane-hpaio.la")

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")
    pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/usr/share/applications")
    pisitools.remove("/usr/bin/foomatic-rip")

