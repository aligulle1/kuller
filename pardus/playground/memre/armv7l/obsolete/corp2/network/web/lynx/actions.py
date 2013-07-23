#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="lynx2-8-7"

def setup():
    shelltools.export("CFLAGS", "%(CFLAGS)s -DNCURSES -DNCURSES_MOUSE_VERSION" % autotools.environment)
    shelltools.export("CXXFLAGS", "%(CXXFLAGS)s -DNCURSES -DNCURSES_MOUSE_VERSION" % autotools.environment)

    autotools.configure("--libdir=/etc/lynx \
                         --enable-ipv6 \
                         --enable-widec \
                         --enable-cgi-links \
                         --enable-EXP_PERSISTENT_COOKIES \
                         --enable-prettysrc \
                         --enable-nls-fork \
                         --enable-file-upload \
                         --enable-read-eta \
                         --enable-libjs \
                         --enable-color-style \
                         --enable-scrollbar \
                         --enable-included-msgs \
                         --enable-8bit-toupper \
                         --enable-addrlist-page \
                         --enable-charset-choice \
                         --enable-default-colors \
                         --enable-externs \
                         --enable-internal-links \
                         --enable-justify-elts \
                         --enable-locale-charset \
                         --enable-nested-tables \
                         --enable-persistent-cookies \
                         --enable-source-cache \
                         --enable-warnings \
                         --with-screen=ncursesw \
                         --with-ssl \
                         --with-bzlib \
                         --with-zlib \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES","COPYHEADER","PROBLEMS","README","docs/*","lynx_help/*.txt")
