#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "aalib-1.4.0"

def setup():
    pisitools.dosed("configure.in", "gpm_mousedriver_test=yes", "gpm_mousedriver_test=no")
    autotools.autoreconf("-fi")

    autotools.configure("--without-slang-driver \
                         --with-curses-driver \
                         --without-x11-driver \
                         --without-gpm \
                         --disable-static \
                         --x-includes=%(SysRoot)s/usr/include \
                         --x-libraries=%(SysRoot)s/usr/lib \
                         --with-ncurses=%(SysRoot)s/usr \
                         --with-gnu-ld" % autotools.environment)

def build():
    autotools.make("CC=%(CC)s" % autotools.environment)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*", "COPYING", "ANNOUNCE")

