#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools

WorkDir = "foomatic-db-engine-3.0-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    # The LANG vars aren't reset early enough so when sed tries to use [a-zA-Z], it borks
    shelltools.export("LC_ALL", "C")
    shelltools.export("LANG", "C")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("lib")
    perlmodules.configure()
    perlmodules.make()
    perlmodules.install()
