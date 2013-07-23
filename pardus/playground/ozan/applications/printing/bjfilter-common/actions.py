#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "bjfilter-common"

def install():

    pisitools.insinto("/usr/lib/cups/backend", "usr/lib/cups/backend/canon_parallel")
    pisitools.insinto("/usr/lib/cups/backend", "usr/lib/cups/backend/canon_usb")
    pisitools.insinto("/usr/lib/cups/filter", "usr/lib/cups/filter/pstocanonbj")

    pisitools.dobin("usr/local/bin/bjcups", "/usr/local/bin/")

