#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="gpac"

def setup():
    shelltools.chmod("configure")
    autotools.configure("--enable-amr \
                         --disable-wx \
                         --use-ffmpeg=no \
                         --disable-oss-audio")

def build():
    autotools.make('-j1 OPTFLAGS="%s -fno-strict-aliasing"' % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-lib")

    # No static libs
    pisitools.remove("/usr/lib/libgpac_static.a")

    pisitools.dosym("/usr/bin/MP4Box","/usr/bin/mp4box")
    pisitools.dosym("/usr/bin/MP4Client","/usr/bin/mp4client")

    pisitools.dohtml("doc/*.html")
    pisitools.doman("doc/man/*.1","man1")
