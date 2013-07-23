#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Amateur Radio APRS Server",
                 "tr": "Amatör Radyo APRS Sunucusu"
                })

PID_FILE = "/var/run/aprx.pid"

@synchronized
def start():
    startService(command="/sbin/aprx",
                 pidfile=PID_FILE)

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)

def status():
    return isServiceRunning(PID_FILE)

