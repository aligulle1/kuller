#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "audacity-src-%s-beta" % get.srcVERSION()

def setup():
    autotools.autoreconf()
    autotools.configure("--disable-static \
                         --enable-unicode \
                         --enable-nyquist \
                         --enable-vamp \
                         --enable-ladspa \
                         --with-lib-preference='system local' \
                         --with-wx-version=2.8 \
                         --with-libsamplerate \
                         --with-libvorbis \
                         --with-libmad \
                         --with-libflac \
                         --with-id3tag \
                         --with-soundtouch \
                         --with-libtwolame \
                         --with-portmixer")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/share/doc/audacity", get.srcTAG())
