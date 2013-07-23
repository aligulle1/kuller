#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.export("SAGE_ROOT", get.curDIR())
    shelltools.export("SAGE_VERION", get.srcVERSION())

    pisitools.dosed("setup.py","SITE_PACKAGES =.*",'SITE_PACKAGES ="%s/usr/lib/%s/site-packages"' % (get.installDIR(),get.curPYTHON()))
    pisitools.dodir("/usr/lib/%s/site-packages"  % get.curPYTHON())

    pythonmodules.install()

    pisitools.dodoc("COPYING*", "TROUBLESHOOT*", "README*")
