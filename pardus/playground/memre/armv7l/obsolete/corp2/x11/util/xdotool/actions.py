#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("0.0_", ""))

def build():
    autotools.make()

def install():
    docDir = os.path.join(get.docDIR(), get.srcNAME())

    pisitools.dobin("xdotool")
    pisitools.doman("xdotool.1")

    pisitools.dodoc("CHANGELIST", "COPYRIGHT", "README")
    pisitools.insinto(docDir, "examples")
