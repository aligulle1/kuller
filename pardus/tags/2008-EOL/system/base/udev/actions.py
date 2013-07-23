#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("LDFLAGS", get.LDFLAGS())

    autotools.configure("--exec-prefix=")

def build():
    autotools.make("all")

def install():

    # Default rules are moved from /etc/udev/rules.d to /lib/udev/rules.d
    # http://git.kernel.org/?p=linux/hotplug/udev.git;a=commit;h=282988c4f8a85c28468e6442e86efe51dc71cc93

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These were explicitly not installed in udev-125, so I remove them.
    pisitools.remove("/lib/udev/fstab_import")
    pisitools.remove("/lib/udev/rules.d/79-fstab_import.rules")

    # Manually install gentoo rules
    pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/30-kernel-compat.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/40-gentoo.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/40-video.rules")
    pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/65-permissions.rules")

    # convert group names
    pisitools.dosed("%s/lib/udev/rules.d/*" % get.installDIR(), 'GROUP="uucp"', 'GROUP="dialout"')
    pisitools.dosed("%s/lib/udev/rules.d/*" % get.installDIR(), 'GROUP="floppy"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/*" % get.installDIR(), 'GROUP="lp"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/*" % get.installDIR(), 'GROUP="usb"', 'GROUP="removable"')
    pisitools.dosed("%s/lib/udev/rules.d/*" % get.installDIR(), 'GROUP="cdrom"', 'GROUP="removable"')

    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevinfo")
    pisitools.dosym("/sbin/udevadm", "/usr/bin/udevsettle")

    # create needed directories
    pisitools.dodir("/lib/udev/devices")
    pisitools.dodir("/lib/udev/devices/net")
    pisitools.dodir("/lib/udev/devices/pts")
    pisitools.dodir("/lib/udev/devices/shm")

    pisitools.dodoc("COPYING", "ChangeLog", "README", "TODO")
