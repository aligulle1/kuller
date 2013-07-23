#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-mit-ext \
                            --with-dpms-ext \
                            --with-xf86vmode-ext \
                            --with-xf86gamma-ext \
                            --with-randr-ext \
                            --with-proc-interrupts \
                            --with-xpm \
                            --with-xshm-ext \
                            --with-xdbe-ext \
                            --enable-locking \
                            --with-gle \
                            --with-jpeg \
                            --without-pixbuf \
                            --with-xml \
                            --with-pam \
                            --without-gtk \
                            --without-motif \
                            --without-shadow \
                            --without-kerberos")

def build():
    autotools.make()

def install():
    pisitools.dodir("/etc/pam.d")

    autotools.rawInstall("install_prefix=%s" % get.installDIR())

    # Remove webcollage its pr0n enabled
    pisitools.remove("/usr/libexec/xscreensaver/webcollage")
    pisitools.remove("/usr/share/man/man6/webcollage.6")
    pisitools.remove("/usr/share/xscreensaver/config/webcollage.xml")
