#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sidplay-libs-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("libsidutils/src/ini/ini.cpp", "#include <malloc.h>", "#include <stdlib.h>")

    pisitools.dosed("resid/Makefile.in", "@ACLOCAL@", "${SHELL} %s/%s/resid/missing --run aclocal-1.8" % (get.workDIR(), WorkDir))

    pisitools.dosed("resid/Makefile.in", "@AUTOMAKE@", "${SHELL} %s/%s/resid/missing --run automake-1.8" % (get.workDIR(), WorkDir))

    shelltools.export("CXXFLAGS", "%s -D_GNU_SOURCE" % get.CXXFLAGS())

    autotools.autoreconf("-fi")

    for i in ("libsidplay", "libsidutils", "resid", "builders/hardsid-builder", "builders/resid-builder"):
        autotools.autoreconf("-fi")

    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/resid", "resid/*.h")

    pisitools.dosym("/usr/lib/sidplay/builders/libresid-builder.so.0.0.1", "/usr/lib/libresid-builder.so.0")
    pisitools.dosym("/usr/lib/sidplay/builders/libresid-builder.so.0.0.1", "/usr/lib/libresid-builder.so")

    # Dirty way to install docs
    for dirs in ("libsidplay", "libsidutils", "resid"):
        for files in ("AUTHORS", "ChangeLog", "COPYING", "TODO", "README"):
            shelltools.cd(dirs)
            pisitools.insinto("/usr/share/doc/%s/%s" % (get.srcTAG(), dirs), "%s" % files)
            shelltools.cd("..")
