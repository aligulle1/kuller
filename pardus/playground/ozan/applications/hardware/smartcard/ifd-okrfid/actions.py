#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ifdokrfid_lnx-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("z98_omnikey_rfid.rules", "RUN\+\=\"ok_pcscd_hotplug\.sh\"", "RUN+=\"/lib/udev/ok_pcscd_hotplug.sh\"")

def install():
    pisitools.dodir("%s/usr/lib/pcsc/drivers/ifdokrfid_lnx-2.6.0.bundle" % get.installDIR())
    shelltools.copytree("ifdokrfid_lnx-2.6.0.bundle", "%s/usr/lib/pcsc/drivers/ifdokrfid_lnx-2.6.0.bundle" % get.installDIR())

    pisitools.insinto("/etc", "cmrfid.ini")

    pisitools.dobin("ok_pcscd_hotplug.sh", "/lib/udev")
    pisitools.insinto("/lib/udev/rules.d", "z98_omnikey_rfid.rules", "98-omnikey-rfid.rules")

    pisitools.dodoc("README")
