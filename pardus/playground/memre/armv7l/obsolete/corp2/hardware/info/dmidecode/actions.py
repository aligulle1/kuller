#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", r"(^CFLAGS\s*=)(.*)$", "\\1 %(CFLAGS)s \\2" % autotools.environment)
    pisitools.dosed("Makefile", r"(^LDFLAGS\s*=)(.*)$", "\\1 %(LDFLAGS)s" % autotools.environment)

def build():
    autotools.make('CC="%(CC)s"' % autotools.environment)

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/%s install-bin install-man" % (get.installDIR(), get.defaultprefixDIR()))

    pisitools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "README")
