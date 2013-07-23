#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("test/TEST-*/test.sh", "vmlinuz", "kernel")

def build():
    autotools.make()

def check():
    # Breaks sandbox as it writes to /var/log/dracut.log
    autotools.make("-C test")

def install():
    autotools.rawInstall("DESTDIR=%s sysconfdir=/etc sbindir=/sbin" % get.installDIR())

    pisitools.dodir("/boot/dracut")
    pisitools.dodir("/var/lib/dracut/overlay")

    # Remove unnecessary modules
    for mod in ("01fips", "10rpmversion", "50gensplash", "98selinux",
                "95dasd", "95dasd_mod", "95zfcp", "95znet",
                "90dmsquash-live"):
        pisitools.removeDir("/usr/share/dracut/modules.d/%s" % mod)

    pisitools.insinto("/etc/logrotate.d", "dracut.logrotate", "dracut")

    pisitools.dodoc("COPYING", "README", "TODO", "HACKING", "NEWS", "AUTHORS", "dracut.conf.d/*.example")
