#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-jack \
                         --with-alsa \
                         --with-oss")

def build():
    autotools.make("-j1")

def install():
    pisitools.dobin("rtaudio-config")

    pisitools.dolib("librtaudio.so.4.0.9")
    pisitools.dosym("/usr/lib/librtaudio.so.4.0.9", "/usr/lib/librtaudio.so")
    pisitools.dolib_a("librtaudio.a")

    pisitools.insinto("/usr/include", "*.h")
    pisitools.insinto("/usr/include", "include/*")

    pisitools.dohtml("doc/html/*")

    pisitools.dodoc("readme", "doc/release.txt")
