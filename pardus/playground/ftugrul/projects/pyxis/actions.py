#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def install():
    suffix = os.popen("uname -r").read().strip("\n")
    shelltools.system("/sbin/mkinitramfs kernel=%s --network --rootdir=/ --output=%s/%s" % (suffix, get.workDIR(), get.srcDIR()))

    pisitools.insinto("/tftpboot/pxe/%s-pyxis" % suffix, "/boot/kernel-%s" % suffix)
    pisitools.insinto("/tftpboot/pxe/%s-pyxis" % suffix, "initramfs-%s" % suffix)

    pisitools.insinto("/usr/bin", "pyxis.py")

    pisitools.dodir("/opt/pyxis")

    # latest-pyxis also is used by AdditionalFiles
    pisitools.dosym("%s-pyxis" % suffix, "/tftpboot/pxe/latest-pyxis")

    # tftp works in chroot
    pisitools.dosym("kernel-%s" % suffix,
                    "/tftpboot/pxe/%s-pyxis/latestkernel" % suffix)

    pisitools.dosym("initramfs-%s" % suffix,
                    "/tftpboot/pxe/%s-pyxis/latestinitramfs" % suffix)

