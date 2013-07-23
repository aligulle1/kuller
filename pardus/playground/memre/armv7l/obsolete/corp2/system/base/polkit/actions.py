#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    crosstools.autoreconf("-fi")
    crosstools.configure("--with-pam-module-dir=/lib/security/ \
                          --with-os-type=Pardus \
                          --enable-examples \
                          --localstatedir=/var \
                          --libexecdir=/usr/libexec/polkit-1 \
                          --disable-introspection \
                          --disable-man-pages \
                          --with-gnu-ld \
                          --disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/lib/polkit-1")
    shelltools.chmod("%s/var/lib/polkit-1" % get.installDIR(), mode=00700)
    shelltools.chmod("%s/etc/polkit-1/localauthority" % get.installDIR(), mode=00700)

    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING", "COPYING")
