#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/usr/share/fpcsrc"]

version = get.srcVERSION().split("_")[0]
sourceDir = "%s/%s" % (get.workDIR(), get.srcDIR())

def build():
    # Use the bootstrap compiler
    autotools.make("PP=%s/ppc386 compiler_cycle" % sourceDir)

    # Rebuild compiler using the new compiler
    shelltools.copy("compiler/ppc386", "ppc386.new")
    autotools.make("PP=%s/ppc386.new compiler_cycle" % sourceDir)
    shelltools.unlink("ppc386.new")
    shelltools.copy("compiler/ppc386", "ppc386.new")

    autotools.make("PP=%s/ppc386.new all" % sourceDir)

def install():
    autotools.rawInstall("PP=%s/ppc386.new INSTALL_PREFIX=%s/usr" % (sourceDir, get.installDIR()))
    pisitools.dosym("/usr/lib/fpc/%s/ppc386" % version, "/usr/bin/ppc386")
    pisitools.removeDir("/usr/lib/fpc/lexyacc")

    shelltools.system("%s/usr/lib/fpc/%s/samplecfg /usr/lib/fpc/%s %s/etc" \
                % (get.installDIR(), version, version, get.installDIR()))

    autotools.make("PP=%s/ppc386 clean" % sourceDir)
    shelltools.copytree(".", "%s/usr/share/fpcsrc/" % get.installDIR())
    pisitools.remove("/usr/share/fpcsrc/ppc386")

    pisitools.rename("/usr/share/doc/fpc-%s" % version, get.srcTAG())
    pisitools.dodoc("compiler/COPYING")
