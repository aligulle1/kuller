#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xf86-input-evdev-%s" % get.srcVERSION()

def setup():
    autotools.configure()
    pisitools.dosed("include/Makefile",
                    "(^sdkdir\\s*=\\s*)%(SysRoot)s(.*$)" % autotools.environment,
                    "\\1\\2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
