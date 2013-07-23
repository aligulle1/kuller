#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="%s" % get.srcNAME()

def install():
    # mkdir needed directory
    pisitools.dodir("/usr/lib/R/library")

    shelltools.cd("..")
    shelltools.system("R CMD INSTALL %s -l %s/usr/lib/R/library --no-docs" % (get.srcNAME() ,get.installDIR()))

    # remove conflicts
    pisitools.remove("/usr/lib/R/library/R.css")
