#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s/zekr" % get.ARCH()

def install():

    pisitools.insinto("/usr/share/zekr/dist","dist/*")
    pisitools.insinto("/usr/share/zekr/lib","lib/*")
    pisitools.insinto("/usr/share/zekr/res","res/*")

    pisitools.dobin("zekr.sh","/usr/share/zekr")

    pisitools.dodoc("doc/*.txt","doc/license/*")
