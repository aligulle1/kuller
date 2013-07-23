#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# We are making our own package to support 2.6 kernels
#
# http://www.sfu.ca/~cth/ltmodem/ltmodem-8.31a10.tar.gz   as main directory and
# http://linmodems.technion.ac.il/packages/ltmodem/kernel-2.6/ltmodem-2.6-alk-8.tar.bz2
# as "modules" directory
# After unpacking use the following commands in DOCs directory
#
# rm -rf Installers build* Build* gcc3.txt Examples Suse*
# rm -rf fixscript* slackware srcprep.man scanmodem.man conf*
# rename .man .1 *.man

WorkDir = "ltmodem-8.31_alpha10-alk8"

def setup():
    pisitools.dosed("modules/Makefile", "SUBDIRS=", "M=")

def build():
    shelltools.cd("modules")
    autotools.make("KERNEL_DIR=/usr/src/linux module")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "modules/*.ko")
    pisitools.insinto("/etc/udev/rules.d/", "modules/docs/ltmodem.rules", "55-ltmodem.rules")

    # install utilities
    pisitools.dosbin("utils/lt_*")
    pisitools.insinto("/usr/sbin", "utils/unloading","lt_unloading")

    # install docs
    pisitools.dohtml("DOCs/*")
    pisitools.doman("DOCs/*.1")
    shelltools.unlink("DOCs/*.html")
    pisitools.dodoc("1ST-READ", "DOCs/*")


