#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "frostwire-%s.noarch" % get.srcVERSION()

def install():
    pisitools.insinto("/opt/frostwire", "*")
    pisitools.dosym("/opt/frostwire/runFrostwire.sh", "/usr/bin/frostwire")

    pisitools.insinto("/usr/share/applications", "frostwire.desktop")

    for svn in [".svn","magnet10/.svn"]:
        pisitools.removeDir("/opt/frostwire/root/%s" % svn)

    pisitools.dodoc("changelog", "COPYING", "EULA.txt")
