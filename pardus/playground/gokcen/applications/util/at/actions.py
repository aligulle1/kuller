#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #fix version of "at -V"
    pisitools.dosed("configure.in", "VERSION=\"3\\.1\\.9\"", "VERSION=\"%s\"" % get.srcVERSION())

    autotools.autoconf("-f")
    autotools.configure(" --with-jobdir=/var/spool/at/atjobs \
                          --with-atspool=/var/spool/at/atspool \
                          --with-etcdir=/etc/at")

def build():
    autotools.make()

def install():
    autotools.rawInstall("IROOT=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/%s-%s" % (get.srcNAME(), get.srcVERSION()))
    pisitools.dodoc("README", "ChangeLog", "COPYING", "Problems", "timespec")
