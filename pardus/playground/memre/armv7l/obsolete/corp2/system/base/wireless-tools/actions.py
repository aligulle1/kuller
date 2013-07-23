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

WorkDir="wireless_tools.29"

def setup():
    pisitools.dosed("Makefile", r"(^CC\s*=).*", "\\1 %(CC)s" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^AR\s*=).*", "\\1 %(AR)s" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^RANLIB\s*=).*", "\\1 %(RANLIB)s" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^CFLAGS\s*=).*", "\\1 %(CFLAGS)s \\\\" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^LDFLAGS\s*=).*", "\\1 %(LDFLAGS)s" % crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("PREFIX=%s/usr INSTALL_INC=%s/usr/include INSTALL_MAN=%s/usr/share/man" % (get.installDIR(), get.installDIR(), get.installDIR()))
    pisitools.dosym("/usr/sbin/iwlist", "/usr/bin/iwlist")

    pisitools.dodoc("CHANGELOG.h", "COPYING", "HOTPLUG.txt", "IFRENAME-VS-XXX.txt", "PCMCIA.txt", "README")
