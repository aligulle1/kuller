#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.export("AT_M4DIR", get.curDIR())
    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-mp3x \
                         --disable-static \
                         --enable-shared \
                         --enable-mp3rtp \
                         --enable-nasm")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=\"%s\" pkghtmldir=\"/usr/share/doc/%s/html\"" % (get.installDIR(), get.srcTAG()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "PRESETS.draft", "README", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
