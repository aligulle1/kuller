#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "vdrift-08-05-08"

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    shelltools.cd("bullet-2.66")
    shelltools.system("./configure")
    shelltools.system("jam bulletcollision bulletmath")


def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    scons.make('release=1 \
                destdir="%s" \
                NLS=0 \
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

    pisitools.dodoc("docs/AUTHORS", "doc/ChangeLog", "COPYING", "NEWS", "README", "SConscript", "TODO", "VAMOS.txt")
