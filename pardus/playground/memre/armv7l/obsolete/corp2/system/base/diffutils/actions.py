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

def setup():
    shelltools.chmod("config/*", 0775)
    crosstools.configure("--enable-nls")

    pisitools.dosed("config.h", "(^#define DEFAULT_EDITOR_PROGRAM).*$", r'\1 "vi"')

def build():
    crosstools.make('LDFLAGS="%s"' % get.LDFLAGS())

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "README")

