#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="cdrtools-2.01.01"

def setup():
    pisitools.dosed("DEFAULTS/Defaults.linux", "/opt/schily", "/usr")
    pisitools.dosed("DEFAULTS/Defaults.linux", "/usr/src/linux/include")
    pisitools.dosed("librscg/scsi-remote.c", "/opt/schily", "/usr")

def build():
    autotools.gnuconfig_update()
    autotools.make('CC="%s -D__attribute_const__=const" \
                    COPTX="%s" CPPOPTX="%s" LDOPTX="%s" \
                    LINKMODE=dynamic' % (get.CC(), get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))

def install():
    for app in ["cdrecord","cdda2wav","mkisofs","readcd","rscsi"]:
        pisitools.dobin("%s/OBJ/*/%s" % (app,app))

    for app in ["devdump","isodump","isoinfo","isovfy"]:
        pisitools.dobin("mkisofs/diag/OBJ/*/%s" % app)

    pisitools.insinto("/usr/lib","libs/*/pic/*.so*")

    pisitools.insinto("/usr/include", "incs/*/align.h")
    pisitools.insinto("/usr/include", "incs/*/avoffset.h")
    pisitools.insinto("/usr/include", "incs/*/xconfig.h")
    pisitools.insinto("/usr/include/schily", "include/schily/*.h")
    pisitools.insinto("/usr/include/scg", "include/scg/*.h")

    pisitools.insinto("/etc/default", "rscsi/rscsi.dfl")
    pisitools.insinto("/etc/default", "cdrecord/cdrecord.dfl")

    pisitools.dodoc("ABOUT", "Changelog", "README*")
    pisitools.doman("*/*.1", "*/*.8")
