#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-syslog --with-mysql --sysconfdir=/etc --with-html-doc-root=/var/www/localhost/htdocs")

def build():
    autotools.make()

def install():
    pisitools.dodir("/var/www/localhost/htdocs")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

