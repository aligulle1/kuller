#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="iproute2-%s" % get.srcVERSION().replace('_','-')

def setup():
    pisitools.dosed("Makefile", "-O2", "%s" % get.CFLAGS())
    pisitools.dosed("tc/m_ipt.c", "/usr/local", "/usr")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          SBINDIR=/sbin \
                          DOCDIR=/usr/share/doc/%s \
                          " % (get.installDIR(), get.srcTAG()))

    pisitools.dodir("/usr/sbin")
    pisitools.domove("/sbin/arpd", "/usr/sbin/")
