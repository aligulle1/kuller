#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s \
                                        -D_FILE_OFFSET_BITS=64 \
                                        -D_LARGEFILE_SOURCE \
                                        -D_GNU_SOURCE \
                                        -fPIC" % crosstools.environment
    pisitools.dosed("magic/Makefile.am", "\$(top_builddir)/src/file", "file")
    crosstools.configure("--datadir=/usr/share/misc \
                         --disable-static")

def build():
    crosstools.make()

    shelltools.cd("python")
    crosstools.environment["file"] = "py_magic"
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s \
                                        -I%(RootDir)s/usr/include/python2.6 \
                                        -I../src -g3 -ggdb -fPIC" % crosstools.environment
    shelltools.system("%(CC)s %(CFLAGS)s -c %(file)s.c -o %(file)s.o" % crosstools.environment)

    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s %(file)s.o \
                       -lpython2.6 -L../src/.libs -lmagic -o magic.so" % crosstools.environment)
    shelltools.cd("..")

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # copy magic.so python binding
    shelltools.makedirs("%s/usr/lib/python2.6/site-packages/" % get.installDIR())
    shelltools.copy("python/*so", "%s/usr/lib/python2.6/site-packages/" % get.installDIR() )

    pisitools.dodoc("ChangeLog", "MAINT", "README")
