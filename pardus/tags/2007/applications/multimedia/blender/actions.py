#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/copyleft/gpl.txt'.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("%s/install/linux2/plugins" % get.workDIR())
    shelltools.copytree("source/blender/blenpluginapi", "%s/install/linux2/plugins" % get.workDIR())
    shelltools.move("%s/install/linux2/plugins/blenpluginapi" % get.workDIR(), "%s/install/linux2/plugins/include" % get.workDIR())

def build():
    scons.make()
    shelltools.cd("%s/install/linux2/plugins" % get.workDIR())
    shelltools.chmod("bmake", 0755)
    autotools.make()
    shelltools.cd("../../../")

def install():
    pisitools.dobin("%s/install/linux2/blender" % get.workDIR())
    pisitools.dobin("%s/install/linux2/blenderplayer" % get.workDIR())

    pisitools.doexe("%s/install/linux2/plugins/texture/*.so" % get.workDIR(), "/usr/lib/blender/textures")
    pisitools.doexe("%s/install/linux2/plugins/sequence/*.so" % get.workDIR(), "/usr/lib/blender/sequences")
    pisitools.insinto("%s/install/linux2/plugins/include/*.h" % get.workDIR(), "/usr/include/blender")
    pisitools.insinto("/usr/lib/blender/", "release/scripts")
    pisitools.dodoc("COPYING", "INSTALL", "README")
