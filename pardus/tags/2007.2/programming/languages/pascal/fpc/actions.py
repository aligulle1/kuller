#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "fpc"

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s/usr" % get.installDIR())
    pisitools.dosym("/usr/lib/fpc/%s/ppc386" % get.srcVERSION(), "/usr/bin/ppc386")

    shelltools.system("%s/usr/lib/fpc/%s/samplecfg /usr/lib/fpc/%s %s/etc" \
                % (get.installDIR(), get.srcVERSION(), \
                   get.srcVERSION(), get.installDIR()))

    pisitools.rename("/usr/share/doc/fpc-%s" % get.srcVERSION(), get.srcTAG())
    pisitools.dodoc("compiler/COPYING", "compiler/README*", "fcl/COPYING.*")

    autotools.make("clean")
    pisitools.dodir("/usr/share/fpcsrc")
    for tree in ("compiler", "fcl", "fv", "ide", "installer", "packages", "rtl", "tests", "utils"):
        shelltools.copytree("%s/" % tree, "%s/usr/share/fpcsrc/%s" % (get.installDIR(), tree))
    shelltools.copy("Makefile*", "%s/usr/share/fpcsrc/" % get.installDIR())

    shelltools.system("find %s -name '.svn' -type d -exec rm -rf {} \; 2>/dev/null" % get.installDIR())

