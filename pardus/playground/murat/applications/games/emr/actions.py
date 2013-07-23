#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "emr-3.0"
NoStrip = "/"

def setup():
    pisitools.dosed("Makefile", "EMR_SRC_TAG=", "EMR_SRC_TAG=%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/doc")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "LICENSE")
