#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="gsm-1.0-pl13"

def setup():
    pisitools.dosed("Makefile", r"(^CC\s*=).*", "\\1 %(CC)s -ansi -pedantic" % autotools.environment)
    pisitools.dosed("Makefile", "pardusCFLAGS", get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s bindir=/usr/bin" % get.installDIR())

    for bin in ["tcat","untoast"]:
        pisitools.remove("/usr/bin/%s" % bin)
        pisitools.dosym("toast", "/usr/bin/%s" % bin)

    # Move gsm.h out of gsm subdir
    # pisitools.insinto("/usr/include","inc/gsm.h")
    # pisitools.removeDir("/usr/include/gsm")

    # No static libs
    pisitools.remove("/usr/lib/libgsm.a")

    pisitools.dodoc("ChangeLog", "COPYRIGHT", "MACHINES", "MANIFEST", "README")
