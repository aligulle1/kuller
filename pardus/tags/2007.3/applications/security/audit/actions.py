#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--sbindir=/sbin \
                         --with-apparmor \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # remove RH specific bits
    pisitools.removeDir("/etc/sysconfig/")
    pisitools.removeDir("/etc/rc.d/")

    pythonmodules.fixCompiledPy("/usr/share/system-config-audit")

    pisitools.dodir("/var/log/audit/")
