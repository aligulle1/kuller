#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "brother-dcp135c"

def install():

    pisitools.dobin("usr/local/Brother/Printer/dcp135c/lpd/filterdcp135c", "/usr/local/Brother/Printer/dcp135c/lpd")
    pisitools.dobin("usr/local/Brother/Printer/dcp135c/lpd/brdcp135cfilter", "/usr/local/Brother/Printer/dcp135c/lpd")
    pisitools.dobin("usr/local/Brother/Printer/dcp135c/lpd/psconvertij2", "/usr/local/Brother/Printer/dcp135c/lpd")

    pisitools.dobin("usr/local/Brother/Printer/dcp135c/cupswrapper/cupswrapperdcp135c", "/usr/local/Brother/Printer/dcp135c/cupswrapper")
    pisitools.dobin("usr/local/Brother/Printer/dcp135c/cupswrapper/brcupsconfpt1", "/usr/local/Brother/Printer/dcp135c/cupswrapper")

    pisitools.dobin("usr/bin/brprintconf_dcp135c", "/usr/bin")

    # Install bcm profiles

    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brio06aa.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brio06ab.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brio06ac.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brio06af.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brio06ag.bcm")

    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brdcp135cfunc")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brdcp135crc")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/brPrintListij2")
    pisitools.insinto("/usr/local/Brother/Printer/dcp135c/inf", "usr/local/Brother/Printer/dcp135c/inf/paperinfij2")

    pisitools.dobin("usr/local/Brother/Printer/dcp135c/inf/setupPrintcapij", "/usr/local/Brother/Printer/dcp135c/inf")
