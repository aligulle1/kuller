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

import os
import gzip

def mygzip(_file):
    r_file = open(_file, "r")
    w_file = gzip.GzipFile("%s.gz" % _file, "w", 9)
    w_file.write(r_file.read())
    w_file.flush()
    w_file.close()
    r_file.close()
    os.unlink(_file)

def mygunzip(_file):
    r_file = gzip.GzipFile(_file, "r")
    write_file = _file.replace(".gz", "")
    w_file = open(write_file, "w")
    w_file.write(r_file.read())
    w_file.close()
    r_file.close()
    os.unlink(_file)

def fixUdevRules():
    # udev rules may contain oneliner changes, doing it this way for now not to
    # miss any models. In time it may change into a patch.
    oldrules = "55-hpmud.rules"
    newrules = "70-hpmud.rules"

    for f in shelltools.ls("*/*.html"):
        pisitools.dosed(f, oldrules, newrules)

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

def fixFoomaticRip():
    for f in shelltools.ls("ppd/*.ppd.gz"):
        mygunzip(f)
        pisitools.dosed(f.replace(".ppd.gz", ".ppd"), "foomatic-rip-hplip", "foomatic-rip")
        pisitools.dosed(f.replace(".ppd.gz", ".ppd"), "dpi\*FoomaticRIPOptionSetting", "dpi\n*FoomaticRIPOptionSetting")
        mygzip(f.replace(".ppd.gz", ".ppd"))

def setup():
    pisitools.dosed("hpssd.py", "/usr/bin/env python", "/usr/bin/python")
    fixUdevRules()
    fixFoomaticRip()

    autotools.configure("--disable-cups11-build \
                         --disable-foomatic-rip-hplip-install \
                         --enable-gui-build \
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
    autotools.rawInstall("DESTDIR=%s -j1\
                          hpppddir=/usr/share/cups/model/hplip \
                          ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")
    pisitools.removeDir("/etc/init.d")

