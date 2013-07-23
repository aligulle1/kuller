#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDefault = "on"
serviceDesc = _({"en": "Canon Printer Daemon for CUPS",
                 "tr": "CUPS için Canon Yazıcı Hizmetleri"})

@synchronized
def start():
    startService(command="/usr/sbin/ccpd", donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ccpd", donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/ccpd")
