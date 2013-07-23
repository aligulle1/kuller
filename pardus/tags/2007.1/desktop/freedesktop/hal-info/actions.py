#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--copy --force")
    autotools.aclocal()
    autotools.autoheader()
    autotools.automake("--add-missing --copy")
    autotools.autoconf()

    shelltools.system("glib-gettextize --force --copy")
    shelltools.system("intltoolize --copy --force --automake")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
