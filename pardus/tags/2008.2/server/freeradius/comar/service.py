#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "FreeRadius Server",
                 "tr": "FreeRadius Sunucusu"})
serviceConf = "freeradius"

@synchronized
def start():
    startService(command="/usr/sbin/radiusd",
                 args="-X",
                 pidfile="/var/run/radiusd/radiusd.pid",
                 donotify=True,
                 detach=True,
                 makepid=True,
                 chuid="radiusd:radiusd")

@synchronized
def stop():
    stopService(pidfile="/var/run/radiusd/radiusd.pid", \
                command="/usr/sbin/radiusd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/radiusd", \
                            pidfile="/var/run/radiusd/radiusd.pid")
