#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--homedir=/etc/dcc \
                            --libexecdir=/usr/sbin \
                            --bindir=/usr/sbin \
                            --mandir=/usr/share/man \
                            --with-rundir=/var/run/dcc \
                            --with-installroot=%s \
                            --with-uid=root \
                            --disable-dccm \
                            --enable-ipv6" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())

    pisitools.domove("/usr/sbin/cdcc", "/usr/bin")
    pisitools.domove("/usr/sbin/dccproc", "/usr/bin")
    pisitools.domove("/usr/sbin/dccif-test", "/usr/bin")

    pisitools.remove("/usr/sbin/updatedcc")
    pisitools.remove("/usr/sbin/uninstalldcc")

    pisitools.dodoc("CHANGES", "*.html")
