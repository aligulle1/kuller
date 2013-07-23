#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("config.h.in", "showaudio", "mplayer")
    autotools.configure("--sysconfdir=/%s/w3m \
                         --with-editor=/usr/bin/emacs \
                         --with-browser=/usr/bin/firefox \
                         --with-termlib=ncurses \
                         --enable-alarm \
                         --enable-ansi-color \
                         --enable-bgcolor \
                         --enable-color \
                         --enable-cookie \
                         --enable-dict \
                         --enable-digest-auth \
                         --enable-external-uri-loader \
                         --enable-gopher \
                         --enable-help-cgi \
                         --enable-history \
                         --enable-image \
                         --enable-ipv6 \
                         --disable-japanese \
                         --disable-kanjisymbols \
                         --enable-keymap=w3m \
                         --enable-menu \
                         --enable-mouse \
                         --enable-nntp \
                         --enable-sslverify \
                         --enable-w3mmailer \
                         --disable-xface \
                         --enable-m17n \
                         --enable-unicode \
                         --with-charset=UTF-8" % get.confDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
