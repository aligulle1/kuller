#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cndrvcups-capt-1.60"

def setup():
    for dir in ("driver", "backend", "pstocapt", "pstocapt2", "pstocapt3", "ppd", "statusui"):
        shelltools.cd(dir)
        shelltools.system("./autogen.sh --prefix=/%s --enable-shared --disable-static" % get.defaultprefixDIR())
        shelltools.cd("..")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/bin", "libs/captmon/captmon")
    pisitools.insinto("/usr/bin", "libs/captmon2/captmon2")
    pisitools.insinto("/usr/bin", "libs/captfilter")
    pisitools.insinto("/usr/bin", "libs/captdrv")
    pisitools.insinto("/usr/bin", "libs/captemon/captmonlbp5000")
    pisitools.insinto("/usr/bin", "libs/captemon/captmonlbp3300")
    pisitools.insinto("/usr/bin", "libs/captemon/captmoncnac5")
    pisitools.insinto("/usr/bin", "libs/captemon/captmoncnac6")
    pisitools.insinto("/usr/bin", "libs/captemon/captmoncnab6")

    for file in shelltools.ls("libs/ccpddata"):
        pisitools.insinto("/usr/share/ccpd", "libs/ccpddata/%s" % file)

    for file in shelltools.ls("data/"):
        pisitools.insinto("/usr/share/caepcm", "data/%s" % file)

    pisitools.insinto("/usr/share/captemon", "libs/captemon/msgtablelbp5000.xml")
    pisitools.insinto("/usr/share/captemon", "libs/captemon/msgtablelbp3300.xml")
    pisitools.insinto("/usr/share/captemon", "libs/captemon/msgtablecnac5.xml")
    pisitools.insinto("/usr/share/captemon", "libs/captemon/msgtablecnac6.xml")
    pisitools.insinto("/usr/share/captemon", "libs/captemon/msgtablecnab6.xml")

    pisitools.insinto("/usr/share/captmon", "libs/captmon/msgtable.xml")
    pisitools.insinto("/usr/share/captmon2", "libs/captmon2/msgtable2.xml")

    pisitools.dosbin("libs/ccpd")
    pisitools.dosbin("libs/ccpdadmin")

    # Install files from samples directory
    pisitools.insinto("/etc", "samples/ccpd.conf")
    #pisitools.insinto("/etc/init.d", "samples/ccpd")

    # Install shared libraries from libs directory
    pisitools.dolib_so("libs/libcaptfilter.so.1.0.0")
    pisitools.dolib_so("libs/libcaiocaptnet.so.1.0.0")
    pisitools.dolib_so("libs/libcncaptnpm.so.1.0.2")

    # Do symlinks to shared libraries
    pisitools.dosym("/usr/lib/libcaiocaptnet.so.1.0.0", "/usr/lib/libcaiocaptnet.so.1")
    pisitools.dosym("/usr/lib/libcaiocaptnet.so.1.0.0", "/usr/lib/libcaiocaptnet.so")

    pisitools.dosym("/usr/lib/libcaptfilter.so.1.0.0", "/usr/lib/libcaptfilter.so.1")
    pisitools.dosym("/usr/lib/libcaptfilter.so.1.0.0", "/usr/lib/libcaptfilter.so")

    pisitools.dosym("/usr/lib/libcncaptnpm.so.1.0.2", "/usr/lib/libcncaptnpm.so.1")
    pisitools.dosym("/usr/lib/libcncaptnpm.so.1.0.2", "/usr/lib/libcncaptnpm.so")

    # Do doc's
    pisitools.dodoc("README*", "LICENSE*", "COPYING")
