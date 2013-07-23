#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOCONF", "2.57")

    autotools.autoconf()
    autotools.configure("--includedir=/usr/include/gpgme \
                        --with-gpg=/usr/bin/gpg2 \
                        --with-pth=yes \
                        --with-gpgsm=/usr/bin/gpgsm \
                        --disable-test")

def build():
    autotools.make("CFLAGS=\"%s -I../assuan/\"" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO", "VERSION")
