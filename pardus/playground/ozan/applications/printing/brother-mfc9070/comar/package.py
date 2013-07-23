#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/share/cups/model/brmfc9070_cups.ppd"):
        os.system("/usr/local/Brother/cupswrapper/cupswrapperMFC9070-1.0.2 -i")

def preRemove():
    if os.path.exists("/usr/share/cups/model/brmfc9070_cups.ppd"):
        os.system("/usr/local/Brother/cupswrapper/cupswrapperMFC9070-1.0.2 -e")
