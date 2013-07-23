#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.autoreconf() # have a buggy mktime check
    crosstools.configure("--bindir=/bin \
                          --enable-nls")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned binaries
    pisitools.remove("/bin/*-*")

    pisitools.dosym("gawk.1", "/usr/share/man/man1/awk.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "LIMITATIONS", "NEWS", "PROBLEMS", "README")
