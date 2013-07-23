#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/ember"
NoStrip = datadir

def install():
    pisitools.dodir(datadir)

    shelltools.copytree("media", "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("media/user/README", "media/user/LICENSE.txt")
