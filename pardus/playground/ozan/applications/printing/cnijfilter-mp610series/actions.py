#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():

    pisitools.insinto("/usr/share/cups/model", "usr/share/cups/model/canonmp610.ppd")

    pisitools.dolib_so("usr/lib/libcnbpcmcm327.so.6.61.1")
    pisitools.dolib_so("usr/lib/libcnbpcnclapi327.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclbjcmd327.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclui327.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpess327.so.3.0.9")
    pisitools.dolib_so("usr/lib/libcnbpo327.so.1.0.3")

    pisitools.dosym("/usr/lib/libcnbpcmcm327.so.6.61.1", "/usr/lib/libcnbpcmcm327.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm327.so.6.61.1", "/usr/lib/libcnbpcmcm327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclapi327.so.3.3.0", "/usr/lib/libcnbpcnclapi327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi327.so.3.3.0", "/usr/lib/libcnbpcnclapi327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd327.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd327.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclui327.so.3.3.0", "/usr/lib/libcnbpcnclui327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui327.so.3.3.0", "/usr/lib/libcnbpcnclui327.so")
    pisitools.dosym("/usr/lib/libcnbpess327.so.3.0.9", "/usr/lib/libcnbpess327.so.3")
    pisitools.dosym("/usr/lib/libcnbpess327.so.3.0.9", "/usr/lib/libcnbpess327.so")
    pisitools.dosym("/usr/lib/libcnbpo327.so.1.0.3", "/usr/lib/libcnbpo327.so.1")
    pisitools.dosym("/usr/lib/libcnbpo327.so.1.0.3", "/usr/lib/libcnbpo327.so")

    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cifmp610.conf")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnb_3270.tbl")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnbpname327.tbl")

    for f in shelltools.ls("usr/local/bin"):
        pisitools.insinto("/usr/local/bin", "usr/local/bin/%s" % f)

    for f in shelltools.ls("usr/local/share/cngpijmonmp610/pixmaps"):
        pisitools.insinto("/usr/local/share/cngpijmonmp610/pixmaps", "usr/local/share/cngpijmonmp610/pixmaps/%s" % f)

    for f in shelltools.ls("usr/local/share/printuimp610"):
        pisitools.insinto("/usr/local/share/printuimp610", "usr/local/share/printuimp610/%s" % f)
