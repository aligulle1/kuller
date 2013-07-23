#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libversion = get.srcVERSION()

def setup():
    pisitools.dosed("Makefile", "ln -s -f $(PREFIX)/bin/", "ln -s")
    pisitools.dosed("Makefile", "(^all:)", "\\1 libbz2.a bzip2 bzip2recover")

def build():
    crosstools.prepare()

    crosstools.make('-f Makefile-libbz2_so \
                     CC=%(CC)s \
                     AR=%(AR)s \
                     RANLIB=%(RANLIB)s \
                     CFLAGS="%(CFLAGS)s -D_FILE_OFFSET_BITS=64 -fPIC"' % \
                     crosstools.environment)
    crosstools.make('clean')
    crosstools.make('CC=%(CC)s \
                     AR=%(AR)s \
                     RANLIB=%(RANLIB)s' % crosstools.environment)

def install():
    crosstools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    # No static libs
    pisitools.removeDir("/usr/lib")

    pisitools.domove("/usr/bin", "/")
    pisitools.remove("/bin/bzip2")
    pisitools.dodir("/lib")

    shelltools.system("cp -v bzip2-shared %s/bin/bzip2" % get.installDIR())

    for link in ("/bin/bunzip2", "/bin/bzcat"):
        pisitools.remove(link)
        pisitools.dosym("bzip2", link)

    pisitools.dolib("libbz2.so.%s" % libversion, "/lib")

    pisitools.dosym("libbz2.so.1", "/lib/libbz2.so")
    pisitools.dosym("libbz2.so.1.0", "/lib/libbz2.so.1")
    pisitools.dosym("libbz2.so.%s" % libversion, "/lib/libbz2.so.1.0")

    pisitools.dohtml("manual.html")
    pisitools.dodoc("README", "CHANGES", "bzip2.txt")
