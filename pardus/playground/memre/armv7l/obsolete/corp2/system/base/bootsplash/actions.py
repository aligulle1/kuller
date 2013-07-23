#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("Utilities/")
    pisitools.dosed("Makefile", r"(^CC\s*=).*", "\\1 %(CC)s %(CFLAGS)s" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^CFLAGS\s*=).*", "\\1 %(CFLAGS)s -I%(RootDir)s/usr/include/freetype2" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^STRIP\s*=).*", "\\1 %(STRIP)s" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^LDFLAGS\s*=).*", "\\1 %(LDFLAGS)s" % crosstools.environment)

def build():
    crosstools.make("-C Utilities")

def install():
    pisitools.dosbin("Utilities/fbmngplay")
    pisitools.dosbin("Utilities/fbtruetype")

    pisitools.dosbin("Utilities/splash", "/sbin")
    pisitools.dosbin("Utilities/splashpbm", "/sbin")
    pisitools.dosbin("Utilities/fbresolution", "/sbin")
