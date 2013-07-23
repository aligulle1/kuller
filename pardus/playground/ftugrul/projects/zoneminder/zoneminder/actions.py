#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import perlmodules

WorkDir="ZoneMinder-%s" % get.srcVERSION()

def setup():
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())
    autotools.autoreconf("-fi")

    autotools.configure("--prefix=/usr \
                         --with-webuser=apache \
                         --with-webgroup=apache \
                         --with-libarch=/lib \
                         --with-mysql=/usr \
                         --with-ffmpeg \
                         --with-extralibs=-lmp3lame \
                         --with-cgidir=/var/www/zoneminder/cgi-bin \
                         --with-webdir=/var/www/zoneminder/htdocs")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/var/log/zoneminder")
    pisitools.dodir("/var/run/zm")
    pisitools.insinto("/usr/share/zoneminder/db/", "db/*.sql")
    perlmodules.fixLocalPod()
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")
