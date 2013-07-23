#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "\$(PREFIX)/man", "\$(PREFIX)/share/man")

def build():
    autotools.make("-j2 CC=%s AR=%s RANLIB=%s" % (get.CC(), get.AR(), get.RANLIB()))
    autotools.make("-f Makefile-libbz2_so")

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    # No static libs
    pisitools.removeDir("/usr/lib")

    pisitools.domove("/usr/bin/", "/bin/")

    for link in ("/bin/bunzip2", "/bin/bzcat"):
        pisitools.remove(link)
        pisitools.dosym("/bin/bzip2", link)

    pisitools.dolib("libbz2.so.1.0.4", "/lib")
    pisitools.dosym("/lib/libbz2.so.1.0.4", "/lib/libbz2.so")
    pisitools.dosym("/lib/libbz2.so.1.0.4", "/lib/libbz2.so.1")
    pisitools.dosym("/lib/libbz2.so.1.0.4", "/lib/libbz2.so.1.0")

    pisitools.domove("/usr/man","/usr/share/")

    pisitools.dodoc("README", "CHANGES", "Y2K_INFO", "bzip2.txt", "manual.pdf", "manual.html", "manual.ps", "manual_*.html",  "README.COMPILATION.PROBLEMS")
