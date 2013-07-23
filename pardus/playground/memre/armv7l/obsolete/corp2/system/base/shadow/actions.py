#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Clean *.gmo files
    for f in shelltools.ls("%s/po/*.gmo" % get.curDIR()):
        shelltools.unlink(f)

    cache = [ "ac_cv_func_setpgrp_void=yes", ]

    crosstools.configure("--enable-shadowgrp \
                          --without-selinux \
                          --without-audit \
                          --with-libpam \
                          --disable-shared", cache=cache)
                          # FIXME --with-audit \

def build():
    # Rebuild gmo catalogs
    crosstools.make("-C po update-gmo")

    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    # groups come from coreutils package
    pisitools.remove("/usr/share/man/man1/groups.1")
    pisitools.remove("/bin/groups")

    # Conflicts with man-pages
    pisitools.remove("/usr/share/man/man3/getspnam.3")
    pisitools.remove("/usr/share/man/man5/passwd.5")

    pisitools.dodoc("ChangeLog","README","NEWS")

