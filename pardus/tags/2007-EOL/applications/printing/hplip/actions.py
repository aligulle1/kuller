#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

def fixUdevRules():
    # udev rules may contain oneliner changes, doing it this way for now not to
    # miss any models. In time it may change into a patch.
    oldrules = "55-hpmud.rules"
    newrules = "70-hpmud.rules"

    for f in shelltools.ls("Makefile.*"):
        pisitools.dosed(f, oldrules, newrules)

    for root, dirs, files in os.walk("doc"):
        for name in files:
            if name.endswith(".html"):
                f = os.path.join(root, name)
                pisitools.dosed(f, oldrules, newrules)

    shelltools.move("data/rules/%s" % oldrules, "data/rules/%s" % newrules)
    pisitools.dosed("data/rules/%s" % newrules, '"lp"', '"pnp"')
    pisitools.dosed("data/rules/%s" % newrules, '"root"', '"pnp"')
    pisitools.dosed("data/rules/%s" % newrules, '"0666"', '"0660"')

def setup():
    pisitools.dosed("hpssd.py", "/usr/bin/env python", "/usr/bin/python")
    fixUdevRules()

    autotools.configure("--disable-cups11-build \
                         --disable-gui-build \
                         --with-cupsbackenddir=/usr/lib/cups/backend \
                         --enable-doc-build \
                         --enable-network-build \
                         --enable-pp-build \
                         --enable-scan-build \
                         --enable-fax-build \
                         --disable-foomatic-xml-install \
                         --enable-foomatic-ppd-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          hpppddir=/usr/share/cups/model/hplip \
                          ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "doc/images/linux_printing_logo.png", "hplip.png")

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")
    pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/usr/share/applications")
    pisitools.remove("/usr/bin/foomatic-rip")

