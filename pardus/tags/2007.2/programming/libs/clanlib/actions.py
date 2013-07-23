#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

import os

WorkDir = "ClanLib-0.6.5"

def fixfiles(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name == ".cvsignore":
                try:
                    os.unlink(os.path.join(root,name))
                except:
                    pass


def setup():
    pisitools.dosed("Setup/Unix/clanlib-config.in", "@comp_mode@")

    autotools.configure("--enable-dyn \
                         --enable-clansound \
                         --libdir=/usr/lib/clanlib-0.6.5 \
                         --includedir=/usr/include/clanlib-0.6.5 \
                         --enable-network \
                         --enable-asm386 \
                         --enable-x11 \
                         --enable-opengl \
                         --enable-vorbis \
                         --enable-png \
                         --enable-ttf \
                         --enable-mikmod \
                         --enable-joystick \
                         --enable-vidmode")

def build():
    autotools.make()

def install():
    autotools.rawInstall('prefix="%(i)s"/usr \
                          LIB_PREFIX="%(i)s"/usr/lib/clanlib-0.6.5 \
                          INC_PREFIX="%(i)s"/usr/include/clanlib-0.6.5' % {"i": get.installDIR()})

    pisitools.rename("/usr/bin/clanlib-config", "clanlib0.6-config")

    pisitools.dodoc("BUGS", "CODING_STYLE", "HARDWARE", "NEWS", "PATCHES", "PORTING", "README*", "ROADMAP", "INSTALL.linux")

    fixfiles("Documentation/Examples")
    shelltools.copytree("Documentation/Examples", "%s/%s/%s/Examples" % (get.installDIR(), get.docDIR(), get.srcTAG()))

    shelltools.cd("%s/usr/lib/clanlib-0.6.5" % get.installDIR())
    for f in shelltools.ls("*.2"):
        shelltools.sym("clanlib-0.6.5/" + f, "../" + f)

