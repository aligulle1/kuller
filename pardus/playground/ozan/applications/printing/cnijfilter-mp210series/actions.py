#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "cnijfilter-mp210series"

def install():

    pisitools.insinto("/usr/share/cups/model", "usr/share/cups/model/canonmp210.ppd")

    pisitools.dolib_so("usr/lib/libcnbpcmcm316.so.6.61.1")
    pisitools.dolib_so("usr/lib/libcnbpcnclapi316.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclbjcmd316.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclui316.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpess316.so.3.0.9")
    pisitools.dolib_so("usr/lib/libcnbpo316.so.1.0.1")

    pisitools.dosym("/usr/lib/libcnbpcmcm316.so.6.61.1", "/usr/lib/libcnbpcmcm316.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm316.so.6.61.1", "/usr/lib/libcnbpcmcm316.so")
    pisitools.dosym("/usr/lib/libcnbpcnclapi316.so.3.3.0", "/usr/lib/libcnbpcnclapi316.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi316.so.3.3.0", "/usr/lib/libcnbpcnclapi316.so")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd316.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd316.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd316.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd316.so")
    pisitools.dosym("/usr/lib/libcnbpcnclui316.so.3.3.0", "/usr/lib/libcnbpcnclui316.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui316.so.3.3.0", "/usr/lib/libcnbpcnclui316.so")
    pisitools.dosym("/usr/lib/libcnbpess316.so.3.0.9", "/usr/lib/libcnbpess316.so.3")
    pisitools.dosym("/usr/lib/libcnbpess316.so.3.0.9", "/usr/lib/libcnbpess316.so")
    pisitools.dosym("/usr/lib/libcnbpo316.so.1.0.1", "/usr/lib/libcnbpo316.so.1")
    pisitools.dosym("/usr/lib/libcnbpo316.so.1.0.1", "/usr/lib/libcnbpo316.so")

    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cifmp210.conf")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnb_3160.tbl")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnbpname316.tbl")

    for f in shelltools.ls("usr/local/bin/"):
        pisitools.dobin("usr/local/bin/%s" % f, "/usr/local/bin")

    for f in shelltools.ls("usr/local/share/cngpijmonmp210/pixmaps"):
        pisitools.insinto("/usr/local/share/cngpijmonmp210/pixmaps", "usr/local/share/cngpijmonmp210/pixmaps/%s" % f)

    for f in shelltools.ls("usr/local/share/printuimp210"):
        pisitools.insinto("/usr/local/share/printuimp210", "usr/local/share/printuimp210/%s" % f)
