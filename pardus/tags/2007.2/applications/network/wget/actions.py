#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("--with-ssl \
                         --with-nsl \
                         --enable-LFS \
                         --sysconfdir=/etc/wget \
                         --enable-ipv6 \
                         --enable-nls \
                         --prefix=/%s \
                         --host=%s \
                         --mandir=/%s \
                         --infodir=/%s \
                         --datadir=/%s \
                         --localstatedir=/%s \
                        " % (get.defaultprefixDIR(), \
                         get.HOST(), get.manDIR(), \
                         get.infoDIR(), get.dataDIR(), \
                         get.localstateDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "MACHINES", "MAILING-LIST", "NEWS", "README", "TODO", "doc/sample.wgetrc")
