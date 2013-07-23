#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", "-fPIC")
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.autoconf()
    autotools.configure("--bindir=/usr/bin \
                         --sbindir=/sbin \
                         --libexecdir=/usr/lib \
                         --enable-gettext")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR())
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-dev")

    # shared in /lib, static in /usr/lib, ldscript fun too
    pisitools.domove("/usr/lib/lib*.so*", "/lib")

    # remove duplicated so files
    for lib in shelltools.ls("%s/lib/lib*.so.*" % get.installDIR()):
        shelltools.unlink(lib)

    # create needed symlinks
    pisitools.dosym("/lib/libdisk.so", "/lib/libdisk.so.0")
    pisitools.dosym("/lib/libdisk.so", "/lib/libdisk.so.0.0.0")

    pisitools.dosym("/lib/libxcmd.so", "/lib/libxcmd.so.0")
    pisitools.dosym("/lib/libxcmd.so", "/lib/libxcmd.so.0.0.0")

    pisitools.dosym("/lib/libxfs.so", "/lib/libxfs.so.0")
    pisitools.dosym("/lib/libxfs.so", "/lib/libxfs.so.0.0.0")

    pisitools.dosym("/lib/libxlog.so", "/lib/libxlog.so.0")
    pisitools.dosym("/lib/libxlog.so", "/lib/libxlog.so.0.0.0")

    pisitools.dosym("/lib/libhandle.so", "/lib/libhandle.so.1")
    pisitools.dosym("/lib/libhandle.so", "/lib/libhandle.so.1.0.3")

    libtools.gen_usr_ldscript("libhandle.so")
