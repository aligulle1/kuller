#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    autotools.autoreconf()
    autotools.rawConfigure("--libdir=/lib \
                            --enable-fakeroot=%s \
                            --host=%s \
                            --enable-isadir=/lib/security" % (get.installDIR(),get.HOST()))

    # Python stuff in docs gives sandbox problems
    pisitools.dosed("Makefile", "modules doc examples", "modules")

    # Do not build pam_userdb.so ...
    pisitools.dosed("Make.Rules", "^HAVE_NDBM_H=yes", "HAVE_NDBM_H=no")
    pisitools.dosed("Make.Rules", "^HAVE_LIBNDBM=yes" ,"HAVE_LIBNDBM=no")
    pisitools.dosed("Make.Rules", "^HAVE_LIBDB=yes", "HAVE_LIBDB=no")

   # Also edit the configuration file else the wrong include files get used
    pisitools.dosed("_pam_aconf.h", "^#define HAVE_NDBM_H.*$", "/* #undef HAVE_NDBM_H */")
    pisitools.dosed("_pam_aconf.h", "^#define HAVE_DB_H.*$", "/* #undef HAVE_DB_H */")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s LDCONFIG=:" % get.installDIR())

    pisitools.doman("doc/man/*.[0-9]")

    pisitools.removeDir("/usr/share/doc/pam/")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")

    # need this for pam_console
    pisitools.dodir("/var/run/console")
