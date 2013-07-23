#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --bindir=/bin \
                         --enable-perl-regexp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Override the default shell scripts... grep knows how to act
    # based on how it's called
    pisitools.remove("/bin/fgrep")
    pisitools.remove("/bin/egrep")
    pisitools.dosym("/bin/grep", "/bin/egrep")
    pisitools.dosym("/bin/grep", "/bin/fgrep")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
