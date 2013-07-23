#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pisitools.dosed("setup.py", "default.kde", "hicolor")
    pythonmodules.install()
    pisitools.remove("%s/bin/feedback" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/feedback/feedback.py" % get.kdeDIR(), "%s/bin/feedback" % get.kdeDIR())
