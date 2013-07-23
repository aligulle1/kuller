#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # Fixup symlink
    pisitools.remove("%s/bin/migration" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/migration/migration/migration.py" % get.kdeDIR(), "%s/bin/migration" % get.kdeDIR())

    pisitools.dodoc("README", "COPYING")
