#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "cnijfilter-mp520series"

def install():

    pisitools.insinto("/usr/share/cups/model", "usr/share/cups/model/canonmp520.ppd")

    pisitools.dolib_so("usr/lib/libcnbpcmcm328.so.6.61.1")
    pisitools.dolib_so("usr/lib/libcnbpcnclapi328.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclbjcmd328.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclui328.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpess328.so.3.0.9")
    pisitools.dolib_so("usr/lib/libcnbpo328.so.1.0.1")

    pisitools.dosym("/usr/lib/libcnbpcmcm328.so.6.61.1", "/usr/lib/libcnbpcmcm328.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm328.so.6.61.1", "/usr/lib/libcnbpcmcm328.so")
    pisitools.dosym("/usr/lib/libcnbpcnclapi328.so.3.3.0", "/usr/lib/libcnbpcnclapi328.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi328.so.3.3.0", "/usr/lib/libcnbpcnclapi328.so")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd328.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd328.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd328.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd328.so")
    pisitools.dosym("/usr/lib/libcnbpcnclui328.so.3.3.0", "/usr/lib/libcnbpcnclui328.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui328.so.3.3.0", "/usr/lib/libcnbpcnclui328.so")
    pisitools.dosym("/usr/lib/libcnbpess328.so.3.0.9", "/usr/lib/libcnbpess328.so.3")
    pisitools.dosym("/usr/lib/libcnbpess328.so.3.0.9", "/usr/lib/libcnbpess328.so")
    pisitools.dosym("/usr/lib/libcnbpo328.so.1.0.1", "/usr/lib/libcnbpo328.so.1")
    pisitools.dosym("/usr/lib/libcnbpo328.so.1.0.1", "/usr/lib/libcnbpo328.so")

    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cifmp520.conf")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnb_3280.tbl")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnbpname328.tbl")

    for f in shelltools.ls("usr/local/bin"):
        pisitools.insinto("/usr/local/bin", "usr/local/bin/%s" % f)

    for f in shelltools.ls("usr/local/share/cngpijmonmp520/pixmaps"):
        pisitools.insinto("/usr/local/share/cngpijmonmp520/pixmaps", "usr/local/share/cngpijmonmp520/pixmaps/%s" % f)

    for f in shelltools.ls("usr/local/share/printuimp520"):
        pisitools.insinto("/usr/local/share/printuimp520", "usr/local/share/printuimp520/%s" % f)
