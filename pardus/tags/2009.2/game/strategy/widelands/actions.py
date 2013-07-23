#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "widelands"
docdir = "/%s/%s/" % (get.docDIR(), get.srcNAME())
datadir = "/usr/share/widelands"
NoStrip = [datadir]

def setup():
    # SVK usage in utils/buildcat.py causes sandbox violation.
    pisitools.dosed("utils/buildcat.py", "detect_revision\(\)", get.srcVERSION())

    scons.make("build=release \
                build_id=%s \
                install_prefix=/usr \
                bindir=bin \
                buildlocale \
                datadir=share/widelands" % get.srcVERSION())

def build():
    scons.make()

def install():
    pisitools.dodir(datadir)

    pisitools.dobin("widelands")

    for data in ["campaigns", "fonts", "global", "locale", "maps", "music", "pics", "sound", "tribes", "txts", "worlds"]:
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/pixmaps", "pics/wl-ico-64.png", "widelands.png")

    pisitools.insinto(docdir, "doc/geometry", "html")
    for i in ["Makefile", "SConscript"]:
        pisitools.remove("%s/html/%s" % (docdir, i))

    pisitools.dodoc("doc/README*", "ChangeLog", "COPYING", "CREDITS")
