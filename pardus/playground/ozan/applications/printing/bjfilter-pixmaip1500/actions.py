#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "bjfilter-pixmaip1500-2.50-2"

def install():

    pisitools.insinto("/usr/share/cups/model", "usr/share/cups/model/canonpixmaip1500.ppd")

    pisitools.dolib_so("usr/lib/libcnbpcmcm214.so.6.11.1")
    pisitools.dolib_so("usr/lib/libcnbpcnclapi214.so.3.1.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclbjcmd214.so.3.1.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclui214.so.3.1.0")
    pisitools.dolib_so("usr/lib/libcnbpess214.so.2.0.5")
    pisitools.dolib_so("usr/lib/libcnbpo214.so.1.0.11")

    pisitools.dosym("/usr/lib/libcnbpcmcm214.so.6.11.1", "/usr/lib/libcnbpcmcm214.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm214.so.6.11.1", "/usr/lib/libcnbpcmcm214.so")

    pisitools.dosym("/usr/lib/libcnbpcnclapi214.so.3.1.0", "/usr/lib/libcnbpcnclapi214.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi214.so.3.1.0", "/usr/lib/libcnbpcnclapi214.so")

    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd214.so.3.1.0", "/usr/lib/libcnbpcnclbjcmd214.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd214.so.3.1.0", "/usr/lib/libcnbpcnclbjcmd214.so")

    pisitools.dosym("/usr/lib/libcnbpcnclui214.so.3.1.0", "/usr/lib/libcnbpcnclui214.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui214.so.3.1.0", "/usr/lib/libcnbpcnclui214.so")

    pisitools.dosym("/usr/lib/libcnbpess214.so.2.0.5", "/usr/lib/libcnbpess214.so.2")
    pisitools.dosym("/usr/lib/libcnbpess214.so.2.0.5", "/usr/lib/libcnbpess214.so")

    pisitools.dosym("/usr/lib/libcnbpo214.so.1.0.11", "/usr/lib/libcnbpo214.so.1")
    pisitools.dosym("/usr/lib/libcnbpo214.so.1.0.11", "/usr/lib/libcnbpo214.so")

    pisitools.dosym("/usr/lib/libpng12.so.0", "/usr/lib/libpng.so.2")

    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/bjfilterpixmaip1500.conf")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnb_2140.tbl")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnbpname214.tbl")

    pisitools.dobin("usr/local/bin/bjfilterpixmaip1500", "/usr/local/bin")

