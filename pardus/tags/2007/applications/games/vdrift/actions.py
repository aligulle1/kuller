#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "vdrift-2006-10-06-src"

def build():
    shelltools.export("CXX", get.CXX())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    scons.make('release=1 \
                destdir="%s" \
                NLS=1 \
                prefix='' \
                localedir=/usr/share/locale \
                datadir=/usr/share/vdrift \
                bindir=/usr/bin \
                os_cxxflags=1 \
                use_binreloc=0' % get.installDIR())


def install():
    pisitools.dobin("build/vdrift")
    pisitools.dodoc("docs/*")

