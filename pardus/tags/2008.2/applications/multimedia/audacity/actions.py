#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "audacity-src-%s" % get.srcVERSION()

def setup():
    shelltools.cd("lib-src/portmixer")
    autotools.autoreconf()
    shelltools.cd("../..")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    autotools.configure("--enable-unicode \
                         --enable-nyquist \
                         --enable-ladspa \
                         --with-lib-preference='system local' \
                         --with-libsndfile=system \
                         --with-libexpat=system \
                         --with-libsamplerate \
                         --with-libvorbis \
                         --with-libmad \
                         --with-libflac \
                         --with-id3tag \
                         --with-soundtouch \
                         --with-libvamp \
                         --with-libtwolame \
                         --with-ffmpeg \
                         --with-redland \
                         --without-slv2 \
                         --with-liblrdf \
                         --with-midi \
                         --with-portmixer \
                         --with-portaudio=v19 \
                         --with-alsa \
                         --with-jack")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/share/doc/audacity", get.srcTAG())
