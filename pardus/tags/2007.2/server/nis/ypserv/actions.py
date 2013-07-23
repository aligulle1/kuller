#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")

    pisitools.insinto("/etc", "etc/ypserv.conf")
    pisitools.insinto("/etc", "etc/netgroup")
    pisitools.insinto("/etc", "etc/netmasks")

    pisitools.insinto("/var/yp", "etc/securenets")
    pisitools.insinto("/var/yp", "etc/securenets.default")
    pisitools.insinto("/var/yp", "Makefile")
