#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.touch("README")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-gl-x11 \
                         --enable-fribidi \
                         --enable-buffer \
                         --enable-software-xlib \
                         --enable-xrender-x11 \
                         --enable-pthreads \
                         --enable-pipe-render \
                         --enable-async-render \
                         --enable-async-events \
                         --enable-async-preload \
                         --with-x \
                         --disable-static")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
