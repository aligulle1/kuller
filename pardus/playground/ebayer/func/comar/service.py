#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Fedora Unified Network Control",
                 "tr": "Fedora birleşik ağ kontrol aracı"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/funcd",
                 args="--daemon",
                 donotify=True)

@synchronized
def stop():
    stopService("/var/run/funcd.pid")

def status():
    return isServiceRunning("/var/run/funcd.pid")
