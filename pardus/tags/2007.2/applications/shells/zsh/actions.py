#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--bindir=/bin \
                         --with-tcsetpgrp \
                         --enable-maildir-support \
                         --enable-etcdir=/etc/zsh \
                         --enable-zshenv=/etc/zsh/zshenv \
                         --enable-zlogin=/etc/zsh/zlogin \
                         --enable-zlogout=/etc/zsh/zlogout \
                         --enable-zprofile=/etc/zsh/zprofile \
                         --enable-zshrc=/etc/zsh/zshrc \
                         --enable-fndir=/usr/share/zsh/%s/functions \
                         --enable-scriptdir=/usr/share/zsh/%s/scripts \
                         --enable-site-fndir=/usr/share/zsh/site-functions \
                         --enable-function-subdirs \
                         --enable-cflags=\"%s\" \
                         --enable-ldflags=\"%s\" \
                         --with-ncurses \
                         --enable-pcre \
                         --enable-caps \
                         --enable-multibyte" % (get.srcVERSION(),get.srcVERSION(),get.CFLAGS(),get.LDFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("Util/*",'/usr/local','/usr')
    pisitools.dosed("Misc/*",'/usr/local','/usr')

    pisitools.insinto("/usr/share/zsh/%s/Util" % get.srcVERSION(),"Util/*")
    pisitools.insinto("/usr/share/zsh/%s/Misc" % get.srcVERSION(),"Misc/*")

    pisitools.doman("Doc/*.1")
    pisitools.dodoc("ChangeLog*","META-FAQ","README","LICENCE","config.modules")

def check():
    autotools.make("ZTST_verbose=0 test")
