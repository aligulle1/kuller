#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#NoStrip = "/"

def unset():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure --mandir=/%s --datadir=/%s \
                       --prefix=/%s \
                       --target=avr \
                       --disable-werror \
                       --disable-nls" % (get.manDIR(), get.dataDIR(), get.defaultprefixDIR()))

def build():
    autotools.make("-C build")

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/man/man1/avr-dlltool.1")
    pisitools.remove("/usr/share/man/man1/avr-nlmconv.1")
    pisitools.remove("/usr/share/man/man1/avr-windres.1")

    # remove multiple binutils info files
    pisitools.remove("/usr/lib/libiberty.a")
    pisitools.removeDir("/usr/share/info")


