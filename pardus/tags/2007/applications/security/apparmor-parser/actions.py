#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "apparmor-parser-2.0.1"

def setup():
    pisitools.dosed("Makefile", "include common/Make.rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/etc/init.d/", "rc.apparmor.slackware", "apparmor")
    shelltools.chmod("%s/etc/init.d/apparmor" % get.installDIR())
