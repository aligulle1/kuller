#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.remove("%s/bin/upgrade-manager" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/upgrade-manager/main.py" % get.kdeDIR(), "%s/bin/upgrade-manager" % get.kdeDIR())


