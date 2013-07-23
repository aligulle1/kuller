# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcNAME()
NoStrip = ["/"]

def install():
    pisitools.dobin("dri/psb_dri.so", "/usr/lib/xorg/modules/dri")
    pisitools.dobin("drivers/Xpsb.so", "/usr/lib/xorg/modules/drivers")

    pisitools.dodoc("COPYING")
