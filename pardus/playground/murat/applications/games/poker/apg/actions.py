#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("standalone")
    autotools.make("-C bfconvert")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s/usr" % get.installDIR())

    pisitools.dohtml("doc/APG_TIPS")
    pisitools.dodoc("COPYING", "CHANGES", "README", "THANKS", "TODO", "doc/*.txt")
