#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tzdata"
tzcode  = "tzcode2010c"
tzdata  = "tzdata2010c"

configTemplate = """
objpfx = %(pwd)s/obj/
sbindir = %(sbindir)s
datadir = %(datadir)s
install_root = %(buildroot)s
sysdep-CFLAGS = %(cflags)s
"""

configVars = {"pwd": "%s/%s" % (crosstools.environment["workDIR"], WorkDir),
              "sbindir": "/%(sbinDIR)s" % crosstools.environment,
              "datadir": "/%(dataDIR)s" % crosstools.environment,
              "buildroot": "%(installDIR)s" % crosstools.environment,
              "cflags": "%(CFLAGS)s" % crosstools.environment
}

def disableLocale():
    for i in ["LANG", "LANGUAGE", "LC_ALL"]:
        shelltools.export(i, "POSIX")

def setup():
    shelltools.sym("Makeconfig.in", "Makeconfig")
    shelltools.echo("config.mk", configTemplate % configVars)
    pisitools.dosed("src/Makefile", r"(^zic-cmd\s*=).*", "\\1 zic -d $(inst_zonedir)")

def build():
    disableLocale()
    crosstools.make("-j1 CROSS_COMPILE=%(target)s" % crosstools.environment)

def install():
    disableLocale()
    crosstools.rawInstall()
    pisitools.removeDir("/etc")

    for i in ["README", "Theory", "tz-link.htm"]:
        pisitools.dodoc("%s/%s" % (tzcode, i))

    # Create Timezone db in /usr/share/zoneinfo
    shelltools.chmod("dump-tz-db", 0755)
    shelltools.system("./dump-tz-db %s" % get.installDIR())

