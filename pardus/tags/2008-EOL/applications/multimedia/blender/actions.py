#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("install/linux2/plugins/include")
    shelltools.copy("source/blender/blenpluginapi/*.h", "install/linux2/plugins/include")

def build():
    scons.make("WITH_BF_PLAYER=1 WITH_BF_OPENAL=1 BF_FANCY=0")
    shelltools.chmod("install/linux2/plugins/bmake", 0755)
    autotools.make("-C install/linux2/plugins")

def install():
    pisitools.insinto("/usr/bin","install/linux2/blender","blender-bin")
    pisitools.dobin("install/linux2/blenderplayer")

    # Install plugins
    pisitools.insinto("/usr/lib/blender/plugins/texture","install/linux2/plugins/texture")
    pisitools.insinto("/usr/lib/blender/plugins/sequence","install/linux2/plugins/sequence")

    # Install miscellaneous files under /usr/lib/blender
    pisitools.insinto("/usr/lib/blender", "release/scripts")
    pisitools.insinto("/usr/lib/blender", "release/scripts/bpydata")
    pisitools.insinto("/usr/lib/blender", "install/linux2/.blender/locale")
    pisitools.insinto("/usr/lib/blender", "install/linux2/.blender/.Blanguages")
    pisitools.insinto("/usr/lib/blender", "install/linux2/.blender/.bfont.ttf")
    pisitools.insinto("/usr/lib/blender", "release/VERSION")

    # chmod 644 for scripts
    shelltools.chmod("%s/usr/lib/blender/scripts/*.py" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/lib/blender/scripts/bpymodules/*.py" % get.installDIR(), 0644)

    # Headers
    pisitools.insinto("/usr/include/blender", "install/linux2/plugins/include/*.h")

    pisitools.dodoc("COPYING", "README")
