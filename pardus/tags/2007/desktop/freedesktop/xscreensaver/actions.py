#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=%s/usr \
                            --with-hackdir=%s/usr/libexec/xscreensaver \
                            --with-configdir=%s/usr/share/xscreensaver/config \
                            --x-libraries=/usr/lib \
                            --x-includes=/usr/include \
                            --with-mit-ext \
                            --with-dpms-ext \
                            --with-xf86vmode-ext \
                            --with-xf86gamma-ext \
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
                            --without-shadow \
                            --without-kerberos" % (get.installDIR(), get.installDIR(), get.installDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
