#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "")

def setup():
    #shelltools.export("WANT_AUTOCONF", "2.5")
    #autotools.autoreconf()
    libtools.libtoolize("--copy --force")

    autotools.configure("--localstatedir=/var \
                         --enable-sandboxed \
                         --disable-debug \
                         --with-transmitter \
                         --with-x \
                         --with-port=0x3f8 \
                         --with-irq=4 \
                         --with-driver=all \
                         --with-syslog=LOG_DAEMON \
                         --with-kerneldir=/usr/src/linux-%s \
                         --with-moduledir=/lib/modules/%s/extra" % (get.curKERNEL(), get.curKERNEL()))

def build():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # example configs
    pisitools.insinto("/etc", "contrib/lircd.conf", "lircd.conf")
    pisitools.insinto("/etc", "contrib/lircmd.conf", "lircmd.conf")

    pisitools.dohtml("doc/html/*.html")
    pisitools.insinto("/usr/share/doc/%s/images" % get.srcTAG(), "doc/images/*")
    pisitools.insinto("/usr/share/doc/%s/contrib" % get.srcTAG(), "contrib/*")

