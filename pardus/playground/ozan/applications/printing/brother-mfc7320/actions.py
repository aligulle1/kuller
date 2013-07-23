#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    shelltools.copytree("usr", "%s/usr" % get.installDIR())

"""
    pisitools.dobin("usr/bin/brprintconf", "/usr/bin")

    pisitools.dobin("usr/local/Brother/lpd/filterMFC7320", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/psconvert", "/usr/local/Brother/lpd")
    pisitools.dobin("usr/local/Brother/lpd/rawtobr", "/usr/local/Brother/lpd")

    pisitools.dobin("usr/local/Brother/cupswrapper/cupswrapperMFC7320-1.0.2", "/usr/local/Brother/cupswrapper")
    pisitools.dobin("usr/local/Brother/cupswrapper/brcupsconfig", "/usr/local/Brother/cupswrapper")

    pisitools.dobin("usr/local/Brother/inf/setupPrintcap", "/usr/local/Brother/inf")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC7320func")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brMFC7320rc")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/brPrintList")
    pisitools.insinto("/usr/local/Brother/inf", "usr/local/Brother/inf/paperinf")

    # Install so file
    pisitools.dolib_so("usr/lib/libbrcomplpr.so")
"""
