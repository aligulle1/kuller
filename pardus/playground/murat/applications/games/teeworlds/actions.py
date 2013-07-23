#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "teeworlds-%s-src" % get.srcVERSION()
datadir = "/usr/share/teeworlds"
NoStrip = [datadir]

def setup():
    pisitools.dosed("default.bam", "pardusCFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    pisitools.dosed("default.bam", "pardusLDFLAGS", get.LDFLAGS())

    shelltools.cd("bam")
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    shelltools.cd("bam")
    autotools.make()
    shelltools.cd("..")

    shelltools.system("bam/src/bam client_release server_release")

def install():
    pisitools.dobin("teeworlds")
    pisitools.dobin("teeworlds_srv")
    pisitools.rename("/usr/bin/teeworlds_srv", "teeworlds-server")

    pisitools.insinto(datadir, "data/*")

    pisitools.dodoc("*.txt")
