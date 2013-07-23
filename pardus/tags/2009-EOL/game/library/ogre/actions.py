#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ogre"

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-freetypetest \
                         --disable-freeimage \
                         --enable-devil \
                         --disable-cg \
                         --enable-openexr \
                         --disable-ogre-demos \
                         --with-x \
                         --with-gl-support=GLX \
                         --with-gui=gtk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("Docs/*.html")
    pisitools.dohtml("Docs/*.gif")

    for dirs in ("Docs/api", "Docs/manual", "Docs/Readme", "Docs/vbo-update"):
        shelltools.copytree(dirs, "%s/%s/%s/html" % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "LINUX.DEV", \
                    "README", "Docs/shadows/OgreShadows.pdf", \
                    "Docs/README.linux", "Docs/licenses/*.txt")
