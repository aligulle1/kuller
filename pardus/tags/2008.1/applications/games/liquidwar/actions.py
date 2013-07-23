#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-doc-ps \
                         --disable-doc-pdf \
                         --disable-target-opt")

    pisitools.dosed("Makefile", "^DOCDIR.*", "DOCDIR = /%s/%s" % (get.docDIR(), get.srcTAG()))

def build():
    autotools.make("-j1")

def install():
    autotools.make("DESTDIR=%s install_nolink" % get.installDIR())
    pisitools.removeDir("/usr/share/applnk")
