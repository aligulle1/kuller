#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
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

    pythonmodules.fixCompiledPy()

    pisitools.dodir("/var/log/audit/")

    #disable zos-remote plugin to get rid of deps. like cyrus-sasl
    pisitools.remove("/etc/audisp/zos-remote.conf")
    pisitools.remove("/etc/audisp/plugins.d/audisp-zos-remote.conf")
    pisitools.remove("/usr/share/man/man8/audispd-zos-remote.8")

    pisitools.dodoc("AUTHORS", "ChangeLog", "THANKS", "TODO", "README", "COPYING")
