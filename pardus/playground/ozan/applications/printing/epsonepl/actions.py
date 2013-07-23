#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("libusb/Makefile.in", "^AM_CFLAGS = .*$", "AM_CFLAGS = $(AM_CFLAGS_EXT)")
    #shelltools.cd("libusb")
    #autotools.configure("--disable-build-docs --disable-shared")
    #shelltools.cd("..")

    autotools.configure()
    #pisitools.dosed("Makefile", "-ansi", "")

def build():
    autotools.make()

def install():
    pisitools.dobin("ijs_server_epsonepl")
    pisitools.dobin("ps2epl.pl")

    # Install CUPS & Foomatic stuff
    for ppd in shelltools.ls("foomatic_PPDs"):
        pisitools.insinto("/usr/share/cups/model/foomatic-db-ppds/Epson", "foomatic_PPDs/%s" % ppd)

    for d in shelltools.ls("foomatic"):
        for f in shelltools.ls("foomatic/%s" % d):
            pisitools.insinto("/usr/share/foomatic/db/source/%s" % d, "foomatic/%s/%s" % (d,f))

    pisitools.dodoc("ChangeLog", "FAQ", "README*", "LIMITATIONS")

