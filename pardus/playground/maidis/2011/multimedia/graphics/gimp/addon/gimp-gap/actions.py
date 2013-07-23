#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-libavformat \
                         --disable-libxvidcore \
                         --disable-audio-support \
                         --with-preinstalled-libmpeg3incdir=/usr/include/libmpeg3 \
                         --with-preinstalled-libmpeg3=/usr/lib/libmpeg3.so")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "docs/howto/txt/*.txt", "docs/reference/txt/*.txt")
