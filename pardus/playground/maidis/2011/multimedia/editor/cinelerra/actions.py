#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--enable-alsa \
               --with-external-ffmpeg \
               --enable-opengl \
               --disable-esd \
               --disable-rpath \
               --disable-static \
               --with-buildinfo=cust/GIT\ Pardus\ build"

    if get.buildTYPE() == "x86_64":
        options += " --disable-mmx"
    else:
        options += " --enable-mmx"

    shelltools.export("AUTOPOINT", "/bin/true")

    # fails due to ‘UINT64_C’ was not declared in this scope - ffmpeg svn related
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())

    # gcc 4.6 workaround from Arch package
    shelltools.export("CFLAGS", "%s -Wwrite-strings" % get.CFLAGS())

    shelltools.system("./autogen.sh")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/include")

    pisitools.rename("/usr/bin/mpeg3cat", "mpeg3cat.hv")
    pisitools.rename("/usr/bin/mpeg3dump", "mpeg3dump.hv")
    pisitools.rename("/usr/bin/mpeg3toc", "mpeg3toc.hv")
    
    pisitools.dosym("/usr/bin/mpeg2enc", "/usr/lib/cinelerra/mpeg2enc") 

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE", "NEWS", "TODO")
