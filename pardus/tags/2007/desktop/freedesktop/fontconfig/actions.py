#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # The date can be troublesome
    pisitools.dosed("configure", "`date`")

    # disable docs only disables docs generation (!)
    autotools.configure("--disable-docs \
                         --disable-static \
                         --with-docdir=/usr/share/doc/%s \
                         --x-includes=/usr/include \
                         --x-libraries=/usr/lib \
                         --localstatedir=/var \
                         --with-cache-dir=/var/cache/fontconfig \
                         --with-default-fonts=/usr/share/fonts" % get.srcTAG())

    # this triggers sandbox, we do this ourselves
    pisitools.dosed("Makefile", "fc-cache/fc-cache -f -v", "sleep 0")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/fonts", "fonts.conf", "fonts.conf.new")

    pisitools.newman("fc-cache/fc-cache.man", "fc-cache.1")
    pisitools.newman("fc-list/fc-list.man", "fc-list.1")
    pisitools.newman("src/fontconfig.man", "fontconfig.3")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    pisitools.dosym("/etc/fonts/conf.avail/01-pardus.conf","/etc/fonts/conf.d/01-pardus.conf")
