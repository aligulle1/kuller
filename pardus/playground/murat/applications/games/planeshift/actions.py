#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/planeshift"

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--datadir=%s \
                         --docdir=/usr/share/doc/%s \
                         --enable-separate-debug-info=no \
                         --with-optimize-debug-info=no \
                         --enable-cpu-specific-optimizations=no \
                         --with-cs-prefix=/usr \
                         --with-cel-prefix=/usr" % (datadir, get.srcTAG()))

def build():
    #pisitools.dosed("Jamconfig", "-O3", get.CXXFLAGS())

    # Let's only build client for now.
    shelltools.system("jam -aq client")

def install():
    shelltools.system("jam -s DESTDIR=%s install_bin" % get.installDIR())

    for data in ["data/npcbehave.xml", "data/npcdefs.xml", "data/pvp_regions.xml"]:
        pisitools.insinto("%s/data" % datadir, data)

    for f in ["eedit.cfg", "npcclient.cfg", "pslaunch.cfg", "psserver.cfg"]:
        pisitools.insinto(datadir, f)

    shelltools.copytree("lang", "%s/%s" % (get.installDIR(), datadir))
    shelltools.copytree("data/eedit", "%s/%s/data" % (get.installDIR(), datadir))
    shelltools.copytree("data/gui", "%s/%s/data" % (get.installDIR(), datadir))

    pisitools.domove("/usr/bin/*", datadir)
    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("docs/*.html")
    pisitools.dodoc("docs/*.txt")
