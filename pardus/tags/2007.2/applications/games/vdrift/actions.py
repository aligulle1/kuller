#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "build/vdrift-2007-03-23-src"

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    scons.make('release=1 \
                destdir="%s" \
                NLS=1 \
                prefix='' \
                localedir=/usr/share/locale \
                datadir=/usr/share/vdrift \
                bindir=/usr/bin \
                os_cc=1 \
                os_cxx=1 \
                os_cxxflags=1 \
                use_binreloc=0' % get.installDIR())


def install():
    pisitools.dobin("build/vdrift")
    pisitools.dodoc("docs/*")

