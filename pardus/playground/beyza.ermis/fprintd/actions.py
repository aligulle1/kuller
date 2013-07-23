#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "V_0_4_1"

def setup():
    shelltools.copy("/usr/share/gtk-doc/data/gtk-doc.make", "%s/V_0_4_1" % get.workDIR())
    autotools.autoreconf("-vfi")

    #workaround for: "error: po/Makefile.in.in was not created by intltoolize." error at the end of configure
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--prefix=/usr --enable-gtk-doc --disable-gtk-doc-html --enable-pam --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "README.transifex")




