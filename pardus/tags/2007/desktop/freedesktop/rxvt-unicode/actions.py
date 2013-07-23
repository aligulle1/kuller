#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --mandir=/usr/share/man \
                            --enable-everything \
                            --enable-perl \
                            --disable-iso14755 \
                            --enable-mousewheel \
                            --enable-slipwheeling \
                            --enable-xft \
                            --enable-font-styles \
                            --enable-xpm-background \
                            --enable-transparency \
                            --enable-tinting \
                            --enable-fading \
                            --enable-smart-resize \
                            --enable-text-blink \
                            --enable-pointer-blank \
                            --enable-utmp \
                            --enable-wtmp \
                            --enable-rxvt-scroll \
                            --enable-next-scroll \
                            --enable-xterm-scroll \
                            --enable-frills")

def build():
    autotools.make()
    pisitools.dosed("doc/rxvt-tabbed", "RXVT_BASENAME = \"rxvt\"", "RXVT_BASENAME = \"urxvt\"")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README.FAQ", "Changes", "doc/README*", "doc/changes.txt", "doc/etc/*", "doc/rxvt-tabbed")
    pisitools.dohtml("doc/*.html")
