#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "lame-398-2"

_build="i686-pc-linux-gnu"
_host="arm-cortex_a8-linux-gnueabi"
_target=_host

# ugly hard-coded stuff, unfortunately..
_RootDir="/pardus-arm"
_ToolchainDir = "/home/memre/x-tools"

# Pardus-ARM preparation
def prepare():
    shelltools.export("LC_ALL", "C")
    shelltools.export("CXXFLAGS", "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("CFLAGS",   "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("LDFLAGS",  "-L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir))

    shelltools.export("CC",     "%s-gcc" % _target)
    shelltools.export("CXX",    "%s-g++" % _target)
    shelltools.export("AR",     "%s-ar"  % _target)
    shelltools.export("AS",     "%s-as"  % _target)
    shelltools.export("LD",     "%s-ld"  % _target)
    shelltools.export("RANLIB", "%s-ranlib"  % _target)
    shelltools.export("OBJDUMP","%s-objdump" % _target)
    shelltools.export("STRIP",  "%s-strip"   % _target)
    shelltools.export("LIBTOOL","%s-libtool" % _target)

def setup():
    # Pardus-ARM preparation
    prepare()

    shelltools.export("AT_M4DIR", get.curDIR())
    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-fi")

    shelltools.makedirs("libmp3lame/i386/.libs")
    autotools.configure("--disable-mp3x \
                         --disable-static \
                         --enable-shared \
                         --disable-mp3rtp \
                         --enable-nasm\
                         --build=%s --host=%s \
                         " % (_build, _host))

def build():
    # Pardus-ARM preparation
    prepare()

    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR="%s" pkghtmldir="/%s/%s/html"' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "README*", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
