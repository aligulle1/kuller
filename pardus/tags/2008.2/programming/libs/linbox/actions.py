#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linbox-1.1.6rc0"

def setup():
    autotools.configure("--enable-doc \
                         --enable-static=no \
                         --with-blas='-L/usr/lib/ -lblas -lgfortran' \
                         --with-atlas=yes \
                         --with-ntl=yes \
                         --with-docdir=/usr/share/doc/%s" % get.srcTAG() )

    pisitools.dosed("interfaces/Makefile", "^SUBDIRS = .*$", "SUBDIRS = driver kaapi")
    pisitools.dosed("doc/Makefile", "^LINBOX_DOC_PATH = .*$", "LINBOX_DOC_PATH = %s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))
    pisitools.dosed("doc/Makefile", "mkdir \$\(docdir\)", "mkdir -p $(docdir)")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
