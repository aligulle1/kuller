#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

design = "%s/%s/design" % (get.docDIR(), get.srcTAG())

def setup():
    shelltools.chmod("doc/*", 0644)
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto(design, "doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB", "README", "RELEASE", "THANKS", "TODO")

