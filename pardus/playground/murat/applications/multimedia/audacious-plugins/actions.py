#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --disable-rpath \
                         --disable-sse2 \
                         --enable-ipv6 \
                         --enable-chardet \
                         --disable-esd \
                         --enable-pulse \
                         --enable-arts \
                         --with-artsc-prefix=%s \
                         --disable-coreaudio \
                         --disable-gconf \
                         --disable-gnomeshortcuts \
                         --enable-amidiplug \
                         --enable-amidiplug-alsa \
                         --disable-amidiplug-flysn \
                         --enable-amidiplug-dummy" % get.kdeDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS")
