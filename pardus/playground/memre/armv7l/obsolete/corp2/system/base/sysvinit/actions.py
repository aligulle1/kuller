#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    crosstools.make("-C src clobber")
    crosstools.make("-C src ROOT=\"%(RootDir)s\" \
                            CC=\"%(CC)s\" \
                            DISTRO=\"Pardus\" \
                            LCRYPT=\"-lcrypt\"" % crosstools.environment)

def install():
    shelltools.cd("src/")
    pisitools.dodir("/dev")
    crosstools.rawInstall("DISTRO=\"Pardus\" ROOT=%s" % get.installDIR())
    pisitools.remove("/dev/initctl")
    pisitools.removeDir("/dev")
