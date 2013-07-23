#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-wx \
                         --use-ffmpeg=no")

def build():
    autotools.make("OPTFLAGS=\"%s -fno-strict-aliasing\"" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-lib")

    # No static libs
    pisitools.remove("/usr/lib/libgpac_static.a")

    pisitools.dosym("/usr/bin/MP4Box","/usr/bin/mp4box")

    pisitools.dohtml("doc/*.html")
    pisitools.doman("doc/man/*.1","man1")
