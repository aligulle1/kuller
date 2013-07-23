#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc \
                         --docdir=%s/%s/%s \
                         --disable-static \
                         --enable-ssl \
                         --enable-nls \
                         --enable-pam" % (get.installDIR(), get.docDIR(), get.srcTAG()))

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("BOOT-ROOT.txt", "FORMAT", "FUTURE", "THANKS")
