#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "libnet"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "VERSION", "doc/BUGS", \
                    "doc/CHANGELOG", "doc/COPYING", \
                    "doc/DESIGN_NOTES", "doc/MIGRATION",\
                    "doc/PACKET_BUILDING" "doc/TODO")
    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/man3/*")
