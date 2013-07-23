#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--localstatedir=/var \
                         --enable-static=no \
                         --enable-usb \
                         --enable-pcsc \
                         --enable-doc \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # udev support
    """
    pisitools.insinto("/etc/udev/rules.d/", "etc/openct.udev", "95-openct-rules")
    pisitools.doexe("etc/openct_pcmcia", "/lib/udev")
    pisitools.doexe("etc/openct_serial", "/lib/udev")
    pisitools.doexe("etc/openct_usb", "/lib/udev")
    """

    # hal support

    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop/", "etc/openct.fdi", "10-usb-openct.fdi")
    pisitools.insinto("/usr/libexec/", "etc/openct.hald", "hald-addon-openct")
    shelltools.chmod("%s/usr/libexec/hald-addon-openct" % get.installDIR())

    pisitools.dodir("/var/run/openct")
    shelltools.chmod("%s/var/run/openct" % get.installDIR(), 0750)
    shelltools.chown("%s/var/run/openct" % get.installDIR(), gid="pnp")

    pisitools.dodoc("NEWS", "TODO", "doc/README")
