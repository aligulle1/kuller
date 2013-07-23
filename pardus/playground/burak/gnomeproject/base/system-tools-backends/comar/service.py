#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "GNOME System Manager",
    "tr": "GNOME Sistem Yöneticisi ",
})
serviceDefault = "on"

@synchronized
def start(boot=True):
    startService(command="/usr/bin/system-tools-backends")

def stop():
    startService(command="/usr/bin/system-tools-backends")

