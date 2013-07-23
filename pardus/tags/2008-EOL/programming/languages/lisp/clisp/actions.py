#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --with-dynamic-ffi \
                            --with-module=wildcard \
                            --with-module=rawsock \
                            --with-module=clx/new-clx \
                            --with-module=pcre \
                            --with-module=zlib \
                            --with-module=dbus")

def build():
    shelltools.cd("src")
    autotools.make("-j1")

def check():
    shelltools.cd("src")
    autotools.make("check")

def install():
    shelltools.cd("src")
    autotools.make("DESTDIR=%s prefix=/usr install-bin" % (get.installDIR()))

    shelltools.cd("..")
    pisitools.dohtml("doc/impnotes.css","doc/impnotes.html","build/clisp.html","doc/clisp.png")
    pisitools.dodoc("doc/editors.txt","doc/CLOS-guide.txt","doc/LISP-tutorial.txt")
