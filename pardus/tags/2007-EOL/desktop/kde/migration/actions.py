#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007, 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    # Fixup symlinks
    for link in "migration", "migration-users":
        pisitools.remove("%s/bin/%s" % (get.kdeDIR(), link))
        pisitools.dosym("%s/share/apps/migration/migration/%s.py" % (get.kdeDIR(), link), "%s/bin/%s" % (get.kdeDIR(), link))

    pisitools.dodoc("README", "COPYING")
