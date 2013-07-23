#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sidplay-libs-%s" % get.srcVERSION()

def setup():
    for i in ("libsidplay", "libsidutils", "resid", "builders/hardsid-builder", "builders/resid-builder"):
        autotools.autoreconf("-fi")

    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/resid", "resid/*.h")

    # Dirty way to install docs
    for dirs in ("libsidplay", "libsidutils", "resid"):
        for files in ("AUTHORS", "ChangeLog", "COPYING", "TODO", "README"):
            shelltools.cd(dirs)
            pisitools.insinto("/usr/share/doc/%s/%s" % (get.srcTAG(), dirs), "%s" % files)
            shelltools.cd("..")
