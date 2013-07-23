#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/share/cups/model/brmfc210c_cups.ppd"):
        os.system("/usr/local/Brother/cupswrapper/cupswrapperMFC210C-1.0.0")

def preRemove():
    if os.path.exists("/usr/share/cups/model/brmfc210c_cups.ppd"):
        os.unlink("/usr/share/cups/model/brmfc210c_cups.ppd")

    if os.path.exists("/usr/lib/cups/filter/brlpdwrapperMFC210C"):
        os.unlink("/usr/lib/cups/filter/brlpdwrapperMFC210C")
