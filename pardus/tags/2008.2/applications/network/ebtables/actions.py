#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ebtables-v2.0.8-2"

dirs = ["/var/lib/ebtables",
        "%s/ebtables" % get.docDIR()]

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    for d in dirs:
        pisitools.dodir(d)

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
