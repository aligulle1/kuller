#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/avrdude.texi", "/usr/local/etc/avrdude.conf", "/etc/avrdude/avrdude.conf")
    pisitools.dosed("avrdude.1", "/etc/avrdude.conf", "/etc/avrdude/avrdude.conf")

    autotools.configure("--enable-doc \
                         --sysconfdir=/etc/avrdude")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.domove("/usr/share/doc/%s-%s/*" % (get.srcNAME(), get.srcVERSION()), "/usr/share/doc/%s" % get.srcNAME())
    pisitools.domove("/usr/share/doc/%s/%s-html" % (get.srcNAME(), get.srcNAME()), "/usr/share/doc/%s/html" % get.srcNAME())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
