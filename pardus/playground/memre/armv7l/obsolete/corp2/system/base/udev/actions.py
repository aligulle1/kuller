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

shelltools.export("HOME", get.workDIR())

def setup():
    cache = [ "ac_cv_file__usr_share_pci_ids=yes",
              "ac_cv_file__usr_share_hwdata_pci_ids=yes",
              "ac_cv_file__usr_share_misc_pci_ids=yes" ]

    # CAUTION!!!
    #
    # While working with Codesurgery toolchain, you have to append -I%(ToolchainDir)s/%(target)s/libc/usr/include
    # whereas with crosstools-ng, you will append -I%(ToolchainDir)s/%(target)s/include
    #

    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -I%(ToolchainDir)s/%(target)s/libc/usr/include" % crosstools.environment

    crosstools.configure("--exec-prefix= \
                         --libexecdir=/lib/udev \
                         --libdir=/usr/lib \
                         --disable-introspection \
                         --enable-logging" % crosstools.environment, cache=cache)

def build():
    crosstools.make('GPERF="gperf -D"')

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These were explicitly not installed in udev-125, so I remove them.
    pisitools.remove("/lib/udev/fstab_import")
    pisitools.remove("/lib/udev/rules.d/79-fstab_import.rules")

    # Let's keep it for a while, I'm not sure (Dropped from Corporate2)
    # pisitools.insinto("/lib/udev/rules.d", "rules/gentoo/40-gentoo.rules")

    # Install additional rules from packages/ directory
    for rule in ("40-pilot-links.rules",):
        pisitools.insinto("/lib/udev/rules.d", "rules/packages/%s" % rule)

    # FIXME: We have GROUP conversions here!
    # Only some gentoo and 50-udev-default.rules are affected by the renamings below

    pisitools.dosed("%s/lib/udev/rules.d/60-floppy.rules" % get.installDIR(), '-G floppy', '-G pnp')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="floppy"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="lp"', 'GROUP="pnp"')
    pisitools.dosed("%s/lib/udev/rules.d/50-udev-default.rules" % get.installDIR(), 'GROUP="cdrom"', 'GROUP="removable"')

    # create needed directories
    for d in ("", "net", "pts", "shm"):
        pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    # Remove gtk-doc
    pisitools.removeDir("/usr/share/gtk-doc")

    # Install docs
    pisitools.dodoc("COPYING", "ChangeLog", "README", "TODO")
