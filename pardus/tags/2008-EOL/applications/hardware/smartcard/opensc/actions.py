#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static=no \
                         --enable-openct \
                         --enable-pcsc \
                         --enable-nsplugin \
                         --with-plugindir=/usr/lib/nsbrowser/plugins/")

    pisitools.dosed("Makefile", "doc\/\${PACKAGE_TARNAME}", "doc/%s" % get.srcTAG())

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc/opensc")

    pisitools.insinto("/etc", "etc/opensc.conf")

    pisitools.dohtml("doc/html.out/*.html")
    pisitools.dodoc("README")
