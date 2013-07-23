#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/etc","examples/synergy.conf")
    shelltools.chmod("%s/etc/synergy.conf" % get.installDIR(), 0644)

    pisitools.dohtml("doc/*.html")
    pisitools.dohtml("doc/images")
    pisitools.dodoc("ChangeLog","COPYING","NEWS","README")
