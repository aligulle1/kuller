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

def setup():
    crosstools.configure("--enable-nls \
                          --bindir=/bin \
                          --without-included-regex \
                          --enable-perl-regexp")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Override the default shell scripts... grep knows how to act
    # based on how it's called
    for f in ["fgrep","egrep"]:
        pisitools.remove("/bin/%s" % f)
        pisitools.dosym("grep", "/bin/%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
