#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 - 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

extras = "extras/scsi_id extras/volume_id extras/ata_id extras/usb_id extras/edd_id extras/dasd_id extras/cdrom_id extras/floppy extras/path_id extras/firmware"

def build():
    autotools.make("V=1 libdir=/lib usrlibdir=/usr/lib OPTFLAGS=\"%s\" EXTRAS=\"%s\" all" % (get.CFLAGS(), extras))

def install():
    autotools.rawInstall("V=1 libdir=/lib usrlibdir=/usr/lib EXTRAS=\"%s\" DESTDIR=%s" % (extras, get.installDIR()))

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    # Use upstream's persistent rules for devices
    pisitools.insinto("/etc/udev/rules.d", "etc/udev/rules.d/60-*.rules")
    pisitools.insinto("/etc/udev/rules.d", "extras/rule_generator/75-*.rules")
    pisitools.doexe("extras/rule_generator/write_*_rules", "lib/udev/")
    pisitools.doexe("extras/rule_generator/rule_generator.functions", "lib/udev/")

    # create needed directories
    pisitools.dodir("/lib/udev/devices")
    pisitools.dodir("/lib/udev/devices/net")
    pisitools.dodir("/lib/udev/devices/pts")
    pisitools.dodir("/lib/udev/devices/shm")

    pisitools.dodoc("COPYING", "ChangeLog", "FAQ", "HOWTO-udev_for_dev", "README", "TODO", "RELEASE-NOTES")
