#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/local/Brother/cupswrapper/cupswrapperMFC7320-2.0.2 -i")

def preRemove():
    os.system("/usr/local/Brother/cupswrapper/cupswrapperMFC7320-2.0.2 -e")
