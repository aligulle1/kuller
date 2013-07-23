#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():

    # Install scanner stuff
    pisitools.dolib_so("usr/lib/libbrcolm.so.1.0.0")
    pisitools.dosym("/usr/lib/libbrcolm.so.1.0.0", "/usr/lib/libbrcolm.so.1")
    pisitools.dosym("/usr/lib/libbrcolm.so.1.0.0", "/usr/lib/libbrcolm.so")

    pisitools.dolib_so("usr/lib/libbrscandec.so.1.0.0")
    pisitools.dosym("/usr/lib/libbrscandec.so.1.0.0", "/usr/lib/libbrscandec.so.1")
    pisitools.dosym("/usr/lib/libbrscandec.so.1.0.0", "/usr/lib/libbrscandec.so")

    pisitools.dolib_so("usr/lib/sane/libsane-brother.so.1.0.7", "/usr/lib/sane")
    pisitools.dosym("/usr/lib/sane/libsane-brother.so.1.0.7", "/usr/lib/sane/libsane-brother.so.1")
    pisitools.dosym("/usr/lib/sane/libsane-brother.so.1.0.7", "/usr/lib/sane/libsane-brother.so")

    pisitools.insinto("/usr/local/Brother/sane", "usr/local/Brother/sane/Brsane.ini")
    pisitools.insinto("/usr/local/Brother/sane", "usr/local/Brother/sane/brsanenetdevice.cfg")

    pisitools.dobin("usr/local/Brother/sane/brsaneconfig", "/usr/local/Brother/sane")
    pisitools.dosym("/usr/local/Brother/sane/brsaneconfig", "/usr/bin/brsaneconfig")

    pisitools.dobin("usr/local/Brother/sane/setupSaneScan", "/usr/local/Brother/sane")

    shelltools.copytree("usr/local/Brother/sane/GrayCmData", "%s/usr/local/Brother/sane/" % get.installDIR())
