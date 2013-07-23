#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s \
                          NO_CHOWN=1 \
                          LIB_INSTALL_DIR=/usr/lib \
                          INC_INSTALL_DIR=/usr/include/svxlink \
                          BIN_INSTALL_DIR=/usr/bin \
                          SBIN_INSTALL_DIR=/usr/sbin \
                          PLUGIN_INSTALL_DIR=/usr/lib/svxlink" % get.installDIR())

    # remove static libraries
    pisitools.remove("/usr/lib/*.a")

    # remove init files as we use COMAR service scripts
    pisitools.removeDir("/etc/init.d")

    # copy sound files.
    pisitools.dodir("/usr/share/svxlink/sounds/en_US")

    shelltools.cd(get.workDIR())
    pisitools.insinto("/usr/share/svxlink/sounds/en_US", "en_US-heather/*")
