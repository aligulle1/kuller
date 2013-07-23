#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

extras = "extras/ata_id extras/cdrom_id extras/collect extras/edd_id extras/firmware extras/floppy extras/path_id extras/rule_generator extras/scsi_id extras/usb_id extras/volume_id"

def build():
    autotools.make('V=1 libdir=/lib usrlibdir=/usr/lib OPTFLAGS="%s" LDFLAGS="%s" EXTRAS="%s" all' % (get.CFLAGS(), get.LDFLAGS(), extras))

def install():
    autotools.rawInstall('V=1 libdir=/lib usrlibdir=/usr/lib EXTRAS="%s" DESTDIR=%s' % (extras, get.installDIR()))

    pisitools.insinto("/etc/udev/rules.d", "etc/udev/gentoo/30-kernel-compat.rules")
    pisitools.insinto("/etc/udev/rules.d", "etc/udev/gentoo/40-gentoo.rules")
    pisitools.insinto("/etc/udev/rules.d", "etc/udev/gentoo/40-video.rules")
    pisitools.insinto("/etc/udev/rules.d", "etc/udev/gentoo/65-permissions.rules")

    # convert group names
    pisitools.dosed("%s/etc/udev/rules.d/*" % get.installDIR(), 'GROUP="uucp"', 'GROUP="dialout"')
    pisitools.dosed("%s/etc/udev/rules.d/*" % get.installDIR(), 'GROUP="floppy"', 'GROUP="pnp"')
    pisitools.dosed("%s/etc/udev/rules.d/*" % get.installDIR(), 'GROUP="lp"', 'GROUP="pnp"')
    pisitools.dosed("%s/etc/udev/rules.d/*" % get.installDIR(), 'GROUP="usb"', 'GROUP="removable"')
    pisitools.dosed("%s/etc/udev/rules.d/*" % get.installDIR(), 'GROUP="cdrom"', 'GROUP="removable"')

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    # create needed directories
    pisitools.dodir("/lib/udev/devices")
    pisitools.dodir("/lib/udev/devices/net")
    pisitools.dodir("/lib/udev/devices/pts")
    pisitools.dodir("/lib/udev/devices/shm")

    pisitools.dodoc("COPYING", "ChangeLog", "FAQ", "HOWTO-udev_for_dev", "README", "TODO", "RELEASE-NOTES")
