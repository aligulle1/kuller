#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip="/usr/share/qemu"

def setup():
    autotools.rawConfigure('--prefix=/usr \
                            --enable-alsa \
                            --disable-gcc-check')

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%(INSTALL_DIR)s/usr \
                          bindir=%(INSTALL_DIR)s/usr/bin \
                          datadir=%(INSTALL_DIR)s/usr/share/qemu \
                          docdir=%(INSTALL_DIR)s/usr/share/doc/%(DOCDIR)s \
                          mandir=%(INSTALL_DIR)s/usr/share/man"
                         % {"INSTALL_DIR" : get.installDIR(), "DOCDIR" : get.srcTAG()})

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")
