#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")

    options = "--with-libwrap \
               --enable-static=no \
               --enable-alsa \
               --enable-ipv6 \
               --enable-oss \
               --disable-arts \
               --disable-dependency-tracking \
               --sysconfdir=/etc/esd"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
        if get.buildTYPE() == "emul32":
	    #install the libraries
            pisitools.insinto("/usr/lib32",".libs/*.so.0.2.39")
            #do the symlinks
            pisitools.dosym("libesd.so.0.2.39","/usr/lib32/libesd.so")
            pisitools.dosym("libesd.so.0.2.39","/usr/lib32/libesd.so.0")
            pisitools.dosym("libesddsp.so.0.2.39","/usr/lib32/libesddsp.so")
            pisitools.dosym("libesddsp.so.0.2.39","/usr/lib32/libesddsp.so.0")
            #make the pkgconfig dir
            pisitools.dodir("/usr/lib32/pkgconfig")
            pisitools.insinto("/usr/lib32/pkgconfig","esound.pc")
        else:
            autotools.rawInstall("DESTDIR=%s" % get.installDIR())

            # Delete the esound library
            pisitools.remove("/usr/bin/esd")
            pisitools.remove("/usr/share/man/man1/esd.1*")

            pisitools.dodoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README", "TIPS", "TODO")

