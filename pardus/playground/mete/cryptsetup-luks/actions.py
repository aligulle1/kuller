#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cryptsetup-%s" % get.srcVERSION()

def builddiet():
    dietCC = "diet %s %s %s -Os -static" % (get.CC(), get.CFLAGS(), get.LDFLAGS())

    shelltools.export("CC", dietCC)
    autotools.make("distclean")
    autotools.autoreconf("-fi")

    autotools.configure("ac_cv_lib_popt_poptConfigFileToString=yes \
                         ac_cv_lib_sepol_sepol_bool_set=no \
                         ac_cv_lib_selinux_is_selinux_enabled=no")

    autotools.make("-C luks")
    autotools.make("-C lib")
    shelltools.system("diet %s %s %s -Os -I./lib -static \
                       -o src/cryptsetup.static src/cryptsetup.c lib/.libs/libcryptsetup.a \
                       -lpopt -lgcrypt -lgpg-error -ldevmapper -luuid -lcompat" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

    pisitools.insinto("/sbin/","src/cryptsetup.static")

def setup():
    # Libs should be installed to /lib because it's possible that /usr
    # is on a different partition other than rootfs.
    # See: http://cvs.fedoraproject.org/viewvc/devel/cryptsetup-luks/cryptsetup-luks.spec?view=co
    autotools.configure("--sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    builddiet()
    pisitools.removeDir("/usr/lib/cryptsetup")

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS", "TODO")
