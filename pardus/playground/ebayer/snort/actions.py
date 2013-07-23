#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc/snort \
                         --disable-static \
                         --enable-dynamicplugin \
                         --enable-build-dynamic-examples \
                         --enable-ipv6 \
                         --enable-zlib \
                         --enable-gre \
                         --enable-targetbased \
                         --enable-ppm \
                         --enable-active-response \
                         --enable-normalizer \
                         --enable-reload \
                         --with-mysql \
                         --with-postgresql")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "LICENSE", "RELEASE.NOTES", "doc/snort_manual.pdf", "doc/snort_schema_v106.pdf", "doc/faq.pdf")
    pisitools.dodoc("schemas")

    # Copy all config dir except MakeFiles
    pisitools.insinto("/etc/snort", "etc/*")
    pisitools.remove("/etc/snort/Makefile*")

    # Create logdir or snort will not start
    pisitools.dodir("/var/log/snort")
