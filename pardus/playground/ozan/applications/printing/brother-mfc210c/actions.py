#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "brother-mfc210c"

def install():


    pisitools.dobin("usr/local/Brother/lpd/filterMFC210C", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/psconvertij2", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/rastertobrij2", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/inf/setupPrintcapij", "/usr/local/Brother/inf")
    pisitools.dobin("usr/local/Brother/cupswrapper/cupswrapperMFC210C-1.0.0", "/usr/local/Brother/cupswrapper")

    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brio04aa.bcm")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brio04ab.bcm")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brio04ac.bcm")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brio04ad.bcm")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC210Cfunc")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC210Crc")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brPrintListij2")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/paperinfij2")

    # Install so file
    pisitools.dolib_so("usr/lib/libbrcompij2.so.1.0.2")

    pisitools.dosym("/usr/lib/libbrcompij2.so.1.0.2", "/usr/lib/libbrcompij2.so.1")
    pisitools.dosym("/usr/lib/libbrcompij2.so.1.0.2", "/usr/lib/libbrcompij2.so")
