#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

def install():

    pisitools.dobin("usr/bin/brprintconf", "/usr/bin")

    pisitools.dobin("usr/local/Brother/lpd/filterMFC9070", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/psconvert", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/rawtobr", "/usr/local/Brother/lpd")

    pisitools.dobin("usr/local/Brother/cupswrapper/cupswrapperMFC9070-1.0.2", "/usr/local/Brother/cupswrapper")
    pisitools.dobin("usr/local/Brother/cupswrapper/brcupsconfig", "/usr/local/Brother/cupswrapper")

    pisitools.dobin("usr/local/Brother/inf/setupPrintcap", "/usr/local/Brother/inf")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC9070func")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC9070rc")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brPrintList")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/paperinf")

    # Install so file
    pisitools.dolib_so("usr/lib/libbrcomplpr.so")
