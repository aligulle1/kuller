#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gsm-1.0-pl12"


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Move gsm.h out of gsm subdir
    pisitools.insinto("/usr/include","inc/gsm.h")
    pisitools.removeDir("/usr/include/gsm")

    pisitools.domove("tcat", "/usr/bin")
    pisitools.domove("toast", "/usr/bin")
    pisitools.domove("untoast", "/usr/bin")

    pisitools.remove("/usr/lib/libgsm.a")

    pisitools.dodoc("ChangeLog", "COPYRIGHT", "INSTALL", "MACHINES", "MANIFEST", "README")
