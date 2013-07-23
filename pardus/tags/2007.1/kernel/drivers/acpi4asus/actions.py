#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="acpi4asus-0.32"

def build():
    autotools.make()

def install():
    pisitools.dobin("asus_acpid/asus_acpid")
    pisitools.doman("asus_acpid/asus_acpid.8")
    pisitools.insinto("/lib/modules/%s/kernel/drivers/acpi" % get.curKERNEL(), "driver/*.ko")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "samples")
    pisitools.chmod("%s/usr/share/doc/acpi4asus-0.32-5/samples/*" % get.installDIR(), 0711)