#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "lightweight network traffic monitor",
                 "tr": "ağ trafik izleyici"})

from comar.service import *

@synchronized
def start():
    startService("/usr/sbin/vnstatd", args="-d",
                 pidfile="/var/run/vnstat.pid", makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/vnstat.pid")

def status():
    return isServiceRunning("/var/run/vnstat.pid")
