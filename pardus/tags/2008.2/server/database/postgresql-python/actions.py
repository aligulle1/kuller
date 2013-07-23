#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ="PyGreSQL-3.8.1"

def install():
     pythonmodules.install()
     pisitools.rename("/usr/lib/%s/site-packages/_pg.so" % get.curPYTHON(), "_pgmodule.so")
     pisitools.dodoc("docs/*")
     pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "tutorial")
