#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for dirs in ("libgsm", "lpc10"):
        shelltools.unlinkDir(dirs)

    autotools.autoreconf("-fi")

    shelltools.export("CFLAGS","%s -fsigned-char" % get.CFLAGS())

    autotools.configure("--disable-static \
                         --disable-largefile \
                         --enable-alsa \
                         --enable-libao \
                         --enable-oss \
                         --with-sndfile \
                         --with-ogg \
                         --with-flac \
                         --with-ffmpeg \
                         --with-mad \
                         --with-id3tag \
                         --with-lame \
                         --with-amr-wb \
                         --with-amr-nb \
                         --with-samplerate \
                         --with-ladspa")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("Changelog", "README", "TODO", "*.txt")
