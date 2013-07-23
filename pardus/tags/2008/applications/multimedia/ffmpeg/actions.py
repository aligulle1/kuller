#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ffmpeg"
version = "14005"

def setup():
    shelltools.export("CFLAGS","%s -DRUNTIME_CPUDETECT" % get.CFLAGS())

    # to keep the source tarball small, write svn version by hand
    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define FFMPEG_VERSION  \\\"SVN-r%s\\\"" > version.h' % version)
    shelltools.chmod("version.sh", 0755)

    # CPU thing is just used for CMOV detection
    autotools.rawConfigure("--cpu=i686 \
                            --prefix=/usr \
                            --mandir=/usr/share/man \
                            --enable-gpl \
                            --enable-swscale \
                            --enable-pthreads \
                            --enable-postproc \
                            --enable-x11grab \
                            --enable-liba52 \
                            --enable-libx264 \
                            --enable-libxvid \
                            --enable-libfaad \
                            --enable-libfaac \
                            --enable-libvorbis \
                            --enable-libmp3lame \
                            --enable-libamr-nb \
                            --enable-libamr-wb \
                            --enable-libdc1394 \
                            --enable-libtheora \
                            --enable-libgsm \
                            --enable-shared \
                            --disable-stripping \
                            --disable-static \
                            --disable-debug")

                            # Not yet
                            # --enable-avfilter \
                            # --enable-avfilter-lavf \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc","doc/ffserver.conf")

    pisitools.dodoc("Changelog", "README")
