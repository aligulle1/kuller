#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "wopengine_src-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("Makefile", "-O3", "%s -DUSE_ACTOR_DEFAULTS" % get.CFLAGS())
    pisitools.dosed("Makefile", "CC=gcc", "CC=%s" % get.CC())

def build():
    autotools.make("BUILD_CLIENT=1 \
                    BUILD_SERVER=1 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_OPENAL_DLOPEN=1 \
                    USE_CURL=1 \
                    USE_CURL_DLOPEN=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_LOCAL_HEADERS=1")

def install():
    pisitools.dobin("build/release-linux-i386/wop-engine.i386")
    pisitools.dobin("build/release-linux-i386/wopded.i386")

    pisitools.rename("/usr/bin/wop-engine.i386", "wop")
    pisitools.rename("/usr/bin/wopded.i386", "wop-server")

    pisitools.dodoc("BUGS", "ChangeLog", "*.txt", "NOTTODO", "TODO", "README")
