#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("0.0_", ""))

def setup():
    pisitools.dosed("Makefile", "CFLAGS=.*", "CFLAGS=%s" % get.CFLAGS())

def build():
    shelltools.export("CC", get.CC())
    autotools.make()

def install():
    docDir = os.path.join(get.docDIR(), get.srcTAG())

    pisitools.dobin("xdotool")
    pisitools.doman("xdotool.1")

    pisitools.dodoc("CHANGELIST", "COPYRIGHT", "README")
    pisitools.insinto(docDir, "examples")
