#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="pavi-"+get.srcVERSION()

def install():
    pisitools.dobin("pavi-"+get.srcVERSION()+".sh")
    pisitools.dosym("/usr/bin/pavi-"+get.srcVERSION()+".sh","/usr/bin/pavi")
    pisitools.dodoc("COPYING","INSTALL","README","*.gif", "*.html", "*.ico", "*.png")
    pisitools.insinto("/etc/init.d/","paviautopatch")
    pisitools.insinto("/usr/share/pixmaps/", "pavi.png")
    pisitools.insinto("/usr/share/pixmaps/", "pavi_root_term.png")